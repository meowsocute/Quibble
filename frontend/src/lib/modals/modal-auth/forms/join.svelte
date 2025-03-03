<script lang="ts">
  import GoogleLogo from '$lib/components/icons/logos/google.svelte';
  import QuibbleTextLogo from '$lib/components/icons/logos/quibble-text.svelte';
  import QuibbleLogo from '$lib/components/icons/logos/quibble.svelte';
  import { toast } from '$lib/components/ui/toast';
  import { cn } from '$lib/functions/classnames';
  import { AuthSchema } from '$lib/schemas/auth';
  import type { FormProps } from '../../types';
  import forms from '../forms';
  import type { HTMLInputAttributes } from 'svelte/elements';
  import { defaults, superForm, type FormResult } from 'sveltekit-superforms';
  import { zod } from 'sveltekit-superforms/adapters';

  let { update_forms_state, goto_form, forms_state }: FormProps<typeof forms> = $props();

  // for persisent data even after navigating b/w forms
  const initial_data = {
    email: (forms_state.join as { email?: string }).email,
    password: (forms_state.join as { password?: string }).password
  };

  const { form, enhance, errors, message, delayed } = superForm(
    defaults(initial_data, zod(AuthSchema)),
    // form options
    {
      resetForm: false,
      validators: zod(AuthSchema),
      onResult({ result }) {
        if (result.type === 'failure' || result.type === 'error') {
          toast.push('Something went wrong! please try again.', { inside_modal: true });
          return;
        }

        if (auth_type === 'login') {
          // save token on forms_state
          update_forms_state('join', {
            token: (result as FormResult<{ data?: { token?: string } }>).data?.token,
            // for persisent form datas
            email: $form.email,
            password: $form.password
          });
          // next form
          goto_form('profile_select');
        } else if (auth_type === 'register') {
          auth_type = 'login';
          // show toast
          toast.push('Suceess! Log in to get started.', { inside_modal: true });
        }
      }
    }
  );

  let auth_type = $state<'login' | 'register'>('login');
  let password_type = $state<HTMLInputAttributes['type']>('password');

  function handle_auth_type_change() {
    auth_type = auth_type === 'login' ? 'register' : 'login';
  }

  function handle_toggle_password_type() {
    password_type = password_type === 'password' ? 'text' : 'password';
  }
</script>

<div class="flex flex-col gap-4">
  <!-- header section -->
  <div class="flex flex-col items-center justify-center gap-4">
    <div class="flex items-center gap-2">
      <QuibbleLogo class="size-7" />
      <QuibbleTextLogo class="h-7 w-auto" />
    </div>
    <p class="text-center font-medium">
      Join in, share your take, and<br /> make some waves!
    </p>
  </div>

  <!-- oauth sections: google -->
  <button class="btn btn-ghost btn-active">
    <GoogleLogo class="size-5" />
    Continue with Google
  </button>
  <div class="divider my-0 text-xs font-bold">OR</div>

  <!-- form element: email and password -->
  <!-- for login and register -->
  <form
    method="POST"
    action="/auth?/{auth_type}"
    use:enhance
    class="flex flex-col gap-3"
    novalidate
  >
    <!-- email input field with errors store -->
    <div class="flex flex-col gap-1">
      <label class="input input-bordered flex items-center gap-2 bg-transparent">
        <coreicons-shape-mail class="size-4"></coreicons-shape-mail>
        <input
          type="email"
          name="email"
          class="grow border-none p-2 text-sm font-medium focus:ring-0"
          placeholder="Email address*"
          bind:value={$form.email}
        />
      </label>

      <!-- error store -->
      {#if $errors.email}
        <span class="flex items-center gap-2 text-error">
          <coreicons-shape-x variant="circle" class="size-3.5"></coreicons-shape-x>
          <span class="text-xs">{$errors.email}</span>
        </span>
      {/if}
    </div>

    <!-- password input field with errors store -->
    <div class="flex flex-col gap-1">
      <label class="input input-bordered flex items-center gap-2 bg-transparent pr-2">
        <coreicons-shape-lock class="size-4"></coreicons-shape-lock>
        <input
          type={password_type}
          name="password"
          class="grow border-none p-2 text-sm font-medium focus:ring-0"
          placeholder="Password*"
          bind:value={$form.password}
        />

        <!-- change password field type to see -->
        <button
          type="button"
          class="btn btn-square btn-ghost btn-sm ml-auto border border-base-content/25 bg-transparent"
          class:btn-active={password_type === 'text'}
          aria-label="Show/hide password"
          onclick={handle_toggle_password_type}
        >
          <coreicons-shape-eye
            class="size-4"
            variant={password_type === 'password' ? 'open' : 'close'}
          ></coreicons-shape-eye>
        </button>
      </label>

      <!-- errors store -->
      {#if $errors.password}
        <span class="flex items-center gap-2 text-error">
          <coreicons-shape-x variant="circle" class="size-3.5"></coreicons-shape-x>
          <span class="text-xs">{$errors.password}</span>
        </span>
      {/if}
    </div>

    <!-- render message store if any, else render help text -->
    <div class="flex items-center gap-2" class:text-error={$message}>
      <coreicons-shape-info class="size-3.5"></coreicons-shape-info>
      <span class="text-xs">{$message ?? `Hint: you can switch b/w 'login' and 'register'.`}</span>
    </div>

    <!-- submit btn with auth type changer -->
    <div class="flex items-center gap-3">
      <button
        type="submit"
        class={cn($delayed && 'btn-active pointer-events-none', 'btn btn-primary flex-1')}
      >
        {auth_type === 'login' ? 'Log in' : 'Register'}

        <!-- delayed store -->
        {#if $delayed}
          <span class="loading loading-spinner loading-xs"></span>
        {:else}
          <coreicons-shape-log-in class="size-4"></coreicons-shape-log-in>
        {/if}
      </button>

      <!-- switch b/w login and register -->
      <button
        type="button"
        class="btn btn-secondary"
        onclick={handle_auth_type_change}
        aria-label="Switch b/w authentication type"
      >
        <coreicons-shape-refresh class="size-4"></coreicons-shape-refresh>
      </button>
    </div>
  </form>

  <!-- footer section -->
  <p class="text-center text-xs">
    By continuing, you agree to the <a
      href="/support/terms-and-conditions"
      class="font-medium text-info">Terms of use</a
    >,
    <a href="/support/privary" class="font-medium text-info">Privacy</a>
    and <a href="/support/policy" class="font-medium text-info">Policy</a> Preplaced.
  </p>
</div>
