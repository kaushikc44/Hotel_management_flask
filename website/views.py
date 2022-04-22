from flask import Blueprint,render_template
from flask_login import login_required,current_user

views = Blueprint('views',__name__)


@views.route('/')
@login_required
def home():
    return  render_template("home.html")

@views.route("/reservation")
@login_required
def reservation():
    return render_template("Reservation.html")