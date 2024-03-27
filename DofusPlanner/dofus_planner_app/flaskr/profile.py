from flask import Blueprint, render_template, request, jsonify, flash, redirect, url_for
from .auth import login_required


profile_bp = Blueprint('profile', __name__)


@profile_bp.route('/profile')
@login_required
def user_profile():
    return render_template('user/profile.html')
