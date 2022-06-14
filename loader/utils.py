import json
from exceptions import WrongImgType

from config import *

def save_picture(picture):
    picture_type = picture.filename.split('.')[-1]
    allowed_type = ['jpg', 'png', 'gif', 'jpeg']
    if picture_type not in allowed_type:
        raise WrongImgType(f"Неверный формат файла: Допустмы только {','.join(allowed_type)}")
    picture_path = (f"{UPLOAD_FOLDER}/{picture.filename}")
    picture.save(picture_path)

    return picture_path

    
def append_new_post_by_json(post_list, post):
    post_list.append(post)
    with open(POST_PATH, 'w', encoding='utf-8') as file:
        json.dump(post_list, file)
    
