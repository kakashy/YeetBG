<script lang="ts">
	import { FileUp } from 'lucide-svelte';

	let dragActive = $state(false);
	let fileInput: HTMLInputElement;

	let { fileSelected } = $props();

	function handleDrag(e: DragEvent) {
		e.preventDefault();
		e.stopPropagation();
		dragActive = e.type === 'dragenter' || e.type === 'dragover';
	}

	function handleDrop(e: DragEvent) {
		e.preventDefault();
		e.stopPropagation();
		dragActive = false;
		if (e.dataTransfer?.files && e.dataTransfer.files[0]) {
			handleFile(e.dataTransfer.files[0]);
		}
	}

	function handleChange(e: Event) {
		e.preventDefault();
		if ((e.target as HTMLInputElement).files) {
			handleFile((e.target as HTMLInputElement).files![0]);
		}
	}

	function handleFile(file: File) {
		if (
			file &&
			file.type.startsWith('image/') &&
			['jpg', 'jpeg', 'png', 'svg'].some((ext) => file.name.toLowerCase().endsWith(ext))
		) {
			fileSelected(file);
		} else {
			alert('Please upload a valid image(jpg, png, or svg)');
		}
	}

	function openFileDialog() {
		fileInput.click();
	}
</script>

<!-- svelte-ignore a11y_click_events_have_key_events -->
<div
	tabindex="0"
	role="button"
	class="from-background via-background to-primary/5 flex h-7 w-full cursor-pointer flex-col items-center justify-center rounded-lg border-2 border-dashed bg-gradient-to-br p-8 text-center transition-colors duration-300 ease-in-out sm:h-fit {dragActive
		? 'border-muted'
		: 'border-muted/60'}"
	class:bg-muted={!dragActive}
	class:bg-background={dragActive}
	ondragenter={handleDrag}
	ondragleave={handleDrag}
	ondragover={handleDrag}
	ondrop={handleDrop}
	onclick={openFileDialog}
>
	<input
		type="file"
		class="hidden"
		accept="image/jpeg,image/png,image/svg+xml"
		onchange={handleChange}
		bind:this={fileInput}
	/>
	<div class="flex flex-col items-center justify-center sm:space-y-4">
		<FileUp />
		<p class="text-xs opacity-70">Please upload your image by clicking or dropping it here.</p>
	</div>
</div>
