export const convertFile = (
	file: File,
	format: 'blob' | 'base64'
): Promise<{ data: string | Blob }> => {
	return new Promise<{ data: string | Blob }>((resolve, reject) => {
		const reader = new FileReader();

		reader.onload = (e: ProgressEvent<FileReader>) => {
			const target = e.target as FileReaderEventTarget & { result: string };

			if (format === 'base64') {
				resolve({ data: target.result as string });
			} else if (format === 'blob') {
				fetch(target.result as string)
					.then((res) => res.blob())
					.then((blob) => resolve({ data: blob }))
					.catch((err) => reject(err));
			}
		};
		reader.onerror = (e) => reject(e);
		reader.readAsDataURL(file);
	});
};

interface FileReaderEventTarget extends EventTarget {
	result: string;
}
