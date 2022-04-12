from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db
from myapp.models import Aquarium
from myapp.aquariums.forms import AquariumForm

aquariums = Blueprint('aquariums', __name__)