from flask import Blueprint, render_template, request
from exceptions import *
from config import POST_PATH
from main.utils import *
import logging

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

logging.basicConfig(filename="logger.log", level=logging.INFO)

@main_blueprint.route('/')
def main_page():
    logging.info("Открытые главной страницы")
    return render_template('index.html')


@main_blueprint.route("/search")
def page_tag():
    s = request.args.get('s', "")
    logging.info("Идёт поиск")
    try:
        posts = loads_json(POST_PATH)
    except DataJsonError:
        return "Проблема с открытием файла постов"
    search_by_post = search_posts_by_substring(posts, s)
    return render_template('post_list.html', posts=search_by_post, s=s)

