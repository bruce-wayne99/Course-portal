from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from app import db

from app.enrolment.models import Enroll

mod_report = Blueprint('enrolment', __name__)

@mod_report.route('/enroll', methods=['POST'])
def enrolled():
    if request.method == 'POST':
        try:
            test = Enroll(request.form['roll'],request.form['id'])
            db.session.add(test)
            db.session.commit()
            return 'sucess: You enrolled a student to a course'
        except:
            return 'error: Enter the values correctly'
