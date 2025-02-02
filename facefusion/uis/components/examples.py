from typing import List, Dict, Optional
import gradio

import os
import facefusion.globals
from facefusion import wording
from facefusion.face_store import clear_static_faces, clear_reference_faces
from facefusion.filesystem import is_image, resolve_relative_path
from facefusion.uis.core import register_ui_component

EXAMPLES_IMAGE: Optional[gradio.Image] = None
EXAMPLES: Optional[gradio.Examples] = None


def render() -> None:
	global EXAMPLES_IMAGE
	global EXAMPLES

	photos_dir = resolve_relative_path('uis/components/photos')
	example_images = load_example_images(photos_dir)

	EXAMPLES_IMAGE = gradio.Image(
		label=wording.get('uis.examples_image'),
		value=None,
		visible=True,
		type='filepath'
	)

	EXAMPLES = gradio.Examples(
		examples=example_images,
		inputs=EXAMPLES_IMAGE,
		examples_per_page=10,
		label=wording.get('uis.examples_image_gallery')
	)

	register_ui_component('examples_image', EXAMPLES_IMAGE)
	register_ui_component('examples', EXAMPLES)


def listen() -> None:
	EXAMPLES_IMAGE.change(update_examples_image, inputs=EXAMPLES_IMAGE, outputs=EXAMPLES_IMAGE)


def update_examples_image(selected_image: str) -> gradio.Image:
	clear_reference_faces()
	clear_static_faces()

	if selected_image and is_image(selected_image):
		facefusion.globals.target_path = selected_image
		return gradio.Image(value=selected_image, visible=True)

	facefusion.globals.target_path = None
	return gradio.Image(value=None, visible=False)


def load_example_images(directory: str) -> List[str]:
	image_paths = list_image_files(directory)
	return [path for path in image_paths if is_image(path)]


def list_image_files(directory: str) -> List[str]:
	image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'}
	image_files = []
	for root, dirs, files in os.walk(directory):
		for file in files:
			if os.path.splitext(file)[1].lower() in image_extensions:
				image_files.append(os.path.join(root, file))
	return image_files
