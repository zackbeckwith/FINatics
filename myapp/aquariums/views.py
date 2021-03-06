from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db
from myapp import photos
from myapp.models import Aquarium
from myapp.aquariums.forms import AquariumForm

aquariums = Blueprint('aquariums', __name__)

@aquariums.route('/create', methods=['GET', 'POST'])
@login_required
def create_aquarium():
  form = AquariumForm()
  if form.validate_on_submit():
    image_file = photos.save(form.image.data)
    aquarium = Aquarium(name = form.name.data, type=form.type.data, fish=form.fish.data, plants=form.plants.data, user_id=current_user.id, image=image_file)
    db.session.add(aquarium)
    db.session.commit()
    flash('Aquarium Created')
    print('Aquarium was created')
    return redirect(url_for('core.home'))
  return render_template('create_aquarium.html', form=form)

@aquariums.route('/<int:aquarium_id>')
def aquarium(aquarium_id):
  aquarium = Aquarium.query.get_or_404(aquarium_id)
  return render_template('aquarium.html', name=aquarium.name, date=aquarium.date, aquarium=aquarium, image=aquarium.image)

@aquariums.route('/<int:aquarium_id>/update',methods=['GET', 'POST'])
@login_required
def update(aquarium_id):
  aquarium = Aquarium.query.get_or_404(aquarium_id)
  if aquarium.owner != current_user:
    abort(403)
  form = AquariumForm()
  if form.validate_on_submit():
    aquarium.name = form.name.data
    aquarium.type = form.type.data
    aquarium.fish = form.fish.data
    aquarium.plants = form.plants.data
    db.session.commit()
    flash('Aquarium Updated')
    return redirect(url_for('aquariums.aquarium', aquarium_id=aquarium.id))
  elif request.method == 'GET':
    form.name.data = aquarium.name
    form.type.data = aquarium.type
    form.fish.data = aquarium.fish
    form.plants.data = aquarium.plants
  return render_template('create_aquarium.html', title='Updating...', form=form)

@aquariums.route('/<int:aquarium_id>/delete',methods=['GET','POST'])
@login_required
def delete_aquarium(aquarium_id):
  aquarium = Aquarium.query.get_or_404(aquarium_id)
  if aquarium.owner != current_user:
    abort(403)
  db.session.delete(aquarium)
  db.session.commit()
  flash('Aquarium Deleted')
  return redirect(url_for('core.home'))