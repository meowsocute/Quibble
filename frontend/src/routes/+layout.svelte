<script lang="ts">
	import '../app.css';
	import { onMount } from 'svelte';
	import { defineCustomElements } from '@coreproject-moe/icons/loader';
	import Header from '$lib/components/header.svelte';
	import Sidebar from '$lib/components/sidebar.svelte';

	let { children } = $props();

	onMount(() => {
		defineCustomElements();
	});
</script>

<main class="flex h-dvh w-dvw flex-col font-sans">
	<Header />
	<section class="flex flex-1 overflow-y-scroll">
		<Sidebar />
		{@render children()}
	</section>
</main>
