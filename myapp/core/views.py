# core/views.py 

from flask import render_template, request, Blueprint
from myapp.models import Aquarium

core = Blueprint('core', __name__)

@core.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    aquariums = Aquarium.query.order_by(Aquarium.date.desc()).paginate(page=page, per_page=5)
    return render_template('index.html', aquariums=aquariums)

@core.route('/info')
def info():
    return render_template('info.html')

