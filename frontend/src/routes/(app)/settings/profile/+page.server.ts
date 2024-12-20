import { fail } from '@sveltejs/kit';
import type { Actions } from './$types';
import { dev } from '$app/environment';
import client from '$lib/clients/client';

export const actions = {
  create: async ({ request, cookies }) => {
    const form_data = await request.formData();

    const { data, error, response } = await client.POST('/api/v1/u/me/profiles/', {
      headers: {
        Authorization: `Bearer ${cookies.get('auth_token')}`
      },
      // @ts-expect-error: only requires username for POST req
      body: {
        username: form_data.get('username') as string
      }
    });

    if (!response.ok && error) {
      return fail(response.status, error.errors[0]);
    } else {
      return data;
    }
  },
  select: async ({ request, cookies }) => {
    const form_data = await request.formData();
    const profile_id = form_data.get('profile_id') as string;

    cookies.set('auth_user_profile_id', profile_id, {
      httpOnly: true,
      secure: !dev,
      path: '/',
      sameSite: 'lax'
    });

    return { success: true };
  }
} satisfies Actions;
