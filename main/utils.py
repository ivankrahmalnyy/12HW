import json
from exceptions import *

def load_json_data(path):
    try:
        with open(path, 'r', encoding="UTF-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        raise DataJsonError
"""
Функция загрузки json в виде словоря
"""

def search_post_by_substring(posts, substring):
    posts_founded = []
    for post in posts:
        if substring.lower() in post["content"].lower():
            posts_founded.append(post)
    return posts_founded
"""
функция поиска по подстроке поста
"""

#print(load_json_data("../posts.json"))