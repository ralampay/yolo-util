import random
import os
import cv2

class Sample:
    def __init__(self, sampled_index=-1, dir_output=''):
        self.sampled_index  = sampled_index
        self.dir_output     = dir_output

    def execute(self):
        img_list    = sorted(os.listdir(f'{self.dir_output}/images'))
        label_list  = sorted(os.listdir(f'{self.dir_output}/labels'))

        num_images = len(img_list)

        if self.sampled_index < 0:
            self.sampled_index = random.randint(0, num_images - 1)

        img_path    = os.path.join(f'{self.dir_output}/images', img_list[self.sampled_index])
        label_path  = os.path.join(f'{self.dir_output}/labels', label_list[self.sampled_index])

        img = cv2.imread(img_path)

        print(f'img_path: {img_path}')
        print(f'label_path: {label_path}')

        dh, dw, _ = img.shape
        
        f = open(label_path, 'r')
        data = f.readlines()
        f.close()

        for dt in data:
            # Split string to float
            print(f'dt: {dt}')
            _, x, y, w, h = map(float, dt.split(' '))

            l = int((x - w / 2) * dw)
            r = int((x + w / 2) * dw)
            t = int((y - h / 2) * dh)
            b = int((y + h / 2) * dh)

            if l < 0:
                l = 0
            if r > dw - 1:
                r = dw - 1
            if t < 0:
                t = 0
            if b > dh - 1:
                b = dh - 1

            print(f'Printing coordinates {(l, t)}, {(r, b)}')
            cv2.rectangle(img, (l, t), (r, b), (0, 0, 255), 3)

        cv2.imshow("Sample Image", img)
        cv2.waitKey()
