from flask import render_template, request, redirect, url_for, abort, flash
from . import main
from ..models import User, Pitch, Comment, Upvote, Downvote
from .. import db,photos
from flask_login import login_required, current_user
from .forms import PitchForm, UpdateProfile, CommentForm

