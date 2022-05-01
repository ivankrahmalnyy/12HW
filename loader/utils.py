import json

from config import UPLOAD_FOLDER,POST_PATH
from exceptions import WrongImgTypr


def save_picture(picture):
    """
    Функция загрузки картинки с проверкой на расширение
    """
    allowed_type = ["jmg", "png", "jpeg", "gif"]
    picture_type = picture.filename.split(".")[-1]
    if picture_type not in allowed_type:
        raise WrongImgTypr(f"Не верный формат файла! Допустимы только {', '.join(allowed_type)}")

    picture_path = f"{UPLOAD_FOLDER}/{picture.filename}"
    picture.save(picture_path)

    return picture_path

def add_post(post_list, post):
    post_list.append(post)
    with open(POST_PATH, "w", encoding="utf-8") as file:
        json.dump(post_list, file)