def get_img_ann(image_id, data):
    img_ann = []
    is_found = False

    for ann in data['annotations']:
        if ann['image_id'] == image_id:
            img_ann.append(ann)
            is_found = True

    return img_ann if is_found else None

def get_img(filename, data):
    for img in data['images']:
        if img['file_name'] == filename:
            return img
