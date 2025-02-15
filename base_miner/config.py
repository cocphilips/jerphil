from pathlib import Path

HUGGINGFACE_CACHE_DIR: Path = Path.home() / '.cache' / 'huggingface'
TARGET_IMAGE_SIZE = (256, 256)


IMAGE_DATASETS = {
    "real": [
        {"path": "bitmind/bm-real"},
        {"path": "bitmind/open-images-v7"},
        {"path": "bitmind/celeb-a-hq"},
        {"path": "bitmind/ffhq-256"},
        {"path": "bitmind/MS-COCO-unique-256"},
        {"path": "evanarlian/imagenet_1k_resized_256"},
        {"path": "philipsnr/aslitrain"},
        {"path": "philipsnr/aslitrain2"},
        {"path": "philipsnr/aslitrain3"},
        {"path": "philipsnr/aslitrain4"},
        {"path": "philipsnr/aslitrain5"}
    ],
    "fake": [
        {"path": "bitmind/bm-realvisxl"},
        {"path": "bitmind/bm-mobius"},
        {"path": "bitmind/bm-sdxl"},
        {"path": "philipsnr/palsutrain"}
    ]
}

# see bitmind-subnet/create_video_dataset_example.sh 
VIDEO_DATASETS = {
    "real": [
        {"path": ""}
    ],
    "fake": [
        {"path": ""}
    ]
}

FACE_IMAGE_DATASETS = {
    "real": [
        {"path": "bitmind/ffhq-256_training_faces", "name": "base_transforms"},
        {"path": "bitmind/celeb-a-hq_training_faces", "name": "base_transforms"},
        {"path": "goodfellowliu/CelebA", "name": "base_transforms"},
        {"path": "philipsnr/muka_asli", "name": "base_transforms"}
    ],
    "fake": [
        {"path": "bitmind/ffhq-256___stable-diffusion-xl-base-1.0_training_faces", "name": "base_transforms"},
        {"path": "bitmind/celeb-a-hq___stable-diffusion-xl-base-1.0___256_training_faces", "name": "base_transforms"},
        {"path": "philipsnr/muka_palsu", "name": "base_transforms"}
    ]
}
