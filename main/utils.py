import json

from exceptions import *



def loads_json(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            loads_json = json.load(file)
        return loads_json
    except (FileNotFoundError, json.JSONDecodeError):
        raise DataJsonError


def search_posts_by_substring(posts, sub):
    sorted_posts = []
    for post in posts:
        if sub.lower() in post['content'].lower():
            sorted_posts.append(post)
    return sorted_posts

