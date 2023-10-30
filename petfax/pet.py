
from flask import Blueprint, render_template
import json

pets = json.load(open('pets.json'))

bp = Blueprint('pet', __name__, url_prefix='/pet')

@bp.route('/')
def index(): 
    return render_template('index.html', pets=pets)
