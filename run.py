#!/usr/bin/env python3

from facefusion import core
from huggingface_hub import snapshot_download

if __name__ == '__main__':
	# local_dir = "./.assets/models"
	# model = 'wanesoft/faceswap_pack'
	# snapshot_download(repo_id=model, local_dir=local_dir, local_files_only=False)
	core.cli()
