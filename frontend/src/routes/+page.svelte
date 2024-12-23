<script lang="ts">
	import { Button } from '$lib/components/ui/button';
	import FileDropInput from '$lib/comps/FileDropInput.svelte';
	import { convertFile } from '$lib/files';
	import { toast } from 'svelte-sonner';
	import { fade } from 'svelte/transition';

	let userImage: string | undefined = $state(undefined);
	let userFile: File;
	let processedImage: string | undefined = $state(undefined);
	let processing = $state(false);

	async function handleFileSelected(file: File) {
		processedImage = undefined;
		userFile = file;
		const prevUser = await convertFile(file, 'base64');
		// let imageBlobPreview = result.data as string;
		let imageBasePreview = prevUser.data as string;
		userImage = imageBasePreview;
	}
	async function handleProcessing() {
		processing = true;
		processedImage = undefined;

		try {
			const formData = new FormData();
			formData.append('image', userFile);

			console.log(userFile);

			const response = () => {
				return fetch('/api/remove-bg', {
					method: 'POST',
					body: formData
				});
			};
			toast.promise(response, {
				loading: 'Processing...',
				success: (data) => {
					handleResponse(data);
					return 'Background removed';
				},
				error: 'Error removing background'
			});
		} catch (err) {}

		processing = false;
	}
	async function handleResponse(rez: { json: () => any }) {
		const data = await rez.json();

		if (data.processedImage) {
			processedImage = data.processedImage;
		} else {
			console.error('Error:', data.error);
		}
	}
</script>

<svelte:head>
	<title>YeetBG</title>
</svelte:head>

<main class="flex w-full flex-col gap-3 p-5">
	<article class="mx-auto mt-5 grid">
		<h1
			class="from-background via-primary/50 to-primary dark:from-primary dark:to-background bg-gradient-to-br bg-clip-text text-center text-[7rem] font-semibold text-transparent"
		>
			YeetBG
		</h1>
	</article>
	<aside class="mx-auto flex max-w-3xl flex-col gap-2 p-5">
		<p class="opacity-90">Please add your image below</p>
		<FileDropInput fileSelected={(file: File) => handleFileSelected(file)} />
		<Button disabled={processing} class="mx-auto my-2" on:click={handleProcessing}
			>Remove background</Button
		>
	</aside>
	<article class="mx-auto flex w-full flex-col items-center gap-2 sm:w-fit sm:flex-row">
		{#if userImage}
			<div class="flex flex-col">
				<p class="font-semibold">Your image input:</p>
				<img
					in:fade={{ duration: 300 }}
					src={userImage}
					class="mx-auto max-h-[50vh] w-fit rounded shadow-lg"
					alt="Your Input File"
				/>
			</div>
		{/if}
		{#if processedImage}
			<div class="mt-4 flex flex-col">
				<p class="font-semibold">Processed image result:</p>
				<img
					in:fade={{ duration: 600 }}
					src={processedImage}
					class="mx-auto max-h-[50vh] w-fit rounded shadow-lg"
					alt="Processed File"
				/>
				<a
					href={processedImage}
					download="processed_image.png"
					class="mt-2 text-center text-blue-600 underline"
				>
					Download Processed Image
				</a>
			</div>
		{/if}
	</article>
</main>
