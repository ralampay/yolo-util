import sys
import argparse
import os

from .utils import get_img, get_img_ann
from .modules.coco_to_yolo import CocoToYolo
from .modules.sample import Sample

def main():
    parser = argparse.ArgumentParser(description='yolo util tool')

    parser.add_argument("--mode", help="Mode", type=str, default="coco-to-yolo")
    parser.add_argument("--dir-images", help="dir images", type=str)
    parser.add_argument("--dir-output", help="dir output", type=str)
    parser.add_argument("--coco-ann", help="coco annotation file", type=str)
    parser.add_argument("--category-ids", help="category ids", type=int, nargs='+', default=[0])
    parser.add_argument("--sampled-index", help="sampled index", type=int, default=-1)

    args = parser.parse_args()

    mode            = args.mode
    dir_images      = args.dir_images
    dir_output      = args.dir_output
    coco_ann        = args.coco_ann
    category_ids    = args.category_ids
    sampled_index   = args.sampled_index

    if mode == "coco-to-yolo": 
        print('Parameters:')
        print(f'coco_ann: {coco_ann}')
        print(f'dir_images: {dir_images}')
        print(f'dir_output: {dir_output}')
        print(f'category_ids: {category_ids}')
        print('===================================')
        
        cmd = CocoToYolo(
            coco_ann=coco_ann,
            dir_images=dir_images,
            dir_output=dir_output,
            category_ids=category_ids,
        )

        cmd.execute()
        print('Done.')

    elif mode == "sample":
        print('Parameters:') 
        print(f'dir_output: {dir_output}')
        print(f'sampled_index: {sampled_index}')
        print('===================================')

        cmd = Sample(
            sampled_index=sampled_index,
            dir_output=dir_output
        )

        cmd.execute()

if __name__ == '__main__':
    main()
