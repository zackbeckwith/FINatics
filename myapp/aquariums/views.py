from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db
from myapp.models import Aquarium
from myapp.aquariums.forms import AquariumForm

aquariums = Blueprint('aquariums', __name__)

@aquariums.route('/create', methods=['GET', 'POST'])
@login_required
def create_aquarium():
  form = AquariumForm()
  if form.validate_on_submit():
    aquarium = Aquarium(name = form.name.data, type=form.type.data, fish=form.fish.data, plants=form.plants.data, user_id=current_user.id)
    db.session.add(aquarium)
    db.session.commit()
    flash('Aquarium Created')
    print('Aquarium was created')
    return redirect(url_for('core.index'))
  return render_template('create_aquarium.html', form=form)

@aquariums.route('/<int:aquarium_id>')
def aquarium(aquarium_id):
  aquarium = Aquarium.query.get_or_404(aquarium_id)
  return render_template('aquarium.html', name=aquarium.name, date=aquarium.date, aquarium=aquarium)

@aquariums.route('/<int:aquarium_id>/update',methods=['GET', 'POST'])
@login_required
def update(aquarium_id):