import shutil
import json
import os
from pylabel import importer

from ..utils import get_img, get_img_ann

class CocoToYolo:
    def __init__(self, coco_ann='', dir_images='', dir_output='', category_ids=[]):
        self.coco_ann       = coco_ann
        self.dir_images     = dir_images
        self.dir_output     = dir_output
        self.category_ids   = category_ids

    def execute(self):
        f = open(self.coco_ann)
        data = json.load(f)
        f.close()

        file_names = []

        # Load images from folder
        for filename in os.listdir(self.dir_images):
            source = os.path.join(self.dir_images, filename)
            destination = f'{self.dir_output}/images/{filename}'

            try:
                shutil.copy(source, destination)
                print(f'File copied to {destination}')
            except shutil.SameFileError:
                print('source and destination represent the same file.')

            file_names.append(filename)

        for filename in file_names:
            img = get_img(filename, data)

            img_id  = img['id']
            img_w   = img['width']
            img_h   = img['height']

            # Get annotations for this img 
            img_ann = get_img_ann(img_id, data)

            if img_ann:
                # Open file for current image
                file_id = filename.split('.')[0]
                file_object = open(f'{self.dir_output}/labels/{file_id}.txt', 'a')

                for ann in img_ann:
                    current_category = ann['category_id'] - 1

                    if current_category in self.category_ids:
                        print(f'current_category: {current_category}')
                        current_bbox = ann['bbox']

                        x = current_bbox[0]
                        y = current_bbox[1]
                        w = current_bbox[2]
                        h = current_bbox[3]

                        # Find midpoints
                        x_center = (2*x + w) / (2*img_w)
                        y_center = (2*y + h) / (2*img_h)
                        w = w / img_w
                        h = h / img_h

                        # Limit up to fix number of decimal places
                        x_center = format(x_center, '.6f')
                        y_center = format(y_center, '.6f')
                        w = format(w, '.6f')
                        h = format(h, '.6f')
                        

                        # write current object 
                        print(f"{current_category} {x_center} {y_center} {w} {h}")
                        file_object.write(f"{current_category} {x_center} {y_center} {w} {h}\n")

                file_object.close()
