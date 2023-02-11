import sys
import argparse
import os

from .utils import get_img, get_img_ann
from .modules.coco_to_yolo import CocoToYolo

def main():
    parser = argparse.ArgumentParser(description='yolo util tool')

    parser.add_argument("--mode", help="Mode", type=str, default="coco-to-yolo")
    parser.add_argument("--dir-images", help="dir images", type=str)
    parser.add_argument("--dir-output", help="dir output", type=str)
    parser.add_argument("--coco-ann", help="coco annotation file", type=str)
    parser.add_argument("--category-ids", help="category ids", type=int, nargs='+', default=[0])

    args = parser.parse_args()

    mode            = args.mode
    dir_images      = args.dir_images
    dir_output      = args.dir_output
    coco_ann        = args.coco_ann
    category_ids    = args.category_ids

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

if __name__ == '__main__':
    main()
