
from flask import Blueprint, render_template, request
import logging
from loader.utils import *
from config import * 
from main.views import loads_json

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')
logging.basicConfig(filename="logger.log", level=logging.INFO)

@loader_blueprint.route('/post', methods=["GET"])
def create_new_post():
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['POST'])
def create_new_post_by_user():
    try:
        picture = request.files.get('picture')
        content = request.form.get('content')
        if not picture or not content:
            logging.info("Данные не загруженны, отсутсвует часть данных")
            return "Отсутствуют данные"    
        posts = loads_json(POST_PATH)
        new_post = {'pic': save_picture(picture), 'content': content}
        append_new_post_by_json(posts, new_post)
        return render_template('post_uploaded.html', new_post=new_post)
    except WrongImgType:
        return "Неверный формат файла"