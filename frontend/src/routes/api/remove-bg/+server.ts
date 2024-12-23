import { json } from '@sveltejs/kit';

/** @type {import('./$types').RequestHandler} */
export async function POST({ request }: { request: Request }) {
	try {
		// Parse the form data
		const formData = await request.formData();
		const file = formData.get('image') as File;

		if (!file) {
			return json({ error: 'No file uploaded' }, { status: 400 });
		}

		// Prepare a new FormData to send to the Python backend
		const backendFormData = new FormData();
		backendFormData.append('file', file); // Key must be 'file'

		// Send the file to the Python backend
		const response = await fetch('http://backend:8000/remove-bg', {
			method: 'POST',
			body: backendFormData
		});

		if (!response.ok) {
			const errorData = await response.json();
			return json(
				{ error: errorData.message || 'Failed to process the image' },
				{ status: response.status }
			);
		}

		const resultBlob = await response.blob();
		const arrayBuffer = await resultBlob.arrayBuffer();
		const base64Image = btoa(
			new Uint8Array(arrayBuffer).reduce((data, byte) => data + String.fromCharCode(byte), '')
		);

		return json({ processedImage: `data:image/png;base64,${base64Image}` });
	} catch (error) {
		console.error('Error in /api/remove-bg:', error);
		return json({ error: 'Internal server error' }, { status: 500 });
	}
}
