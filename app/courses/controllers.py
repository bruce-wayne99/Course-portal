from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from app import db
from flask import jsonify
from app.courses.models import Course
mod_courses = Blueprint('courses', __name__)

@mod_courses.route('/courses', methods=['GET'])
def get_all_courses():
    if request.method == 'GET':
        courses=[]
        list = Course.query.all()
        for num in list:
            req = {
             "id" : num.id,
             "name" : num.name
            }
            courses.append(req)
    return jsonify(courses = courses)
@mod_courses.route('/addCourse', methods=['POST'])
def add_course():
    if request.method == 'POST':
        try:
            course = Course(request.form['id'], request.form['name'])
            db.session.add(course)
            db.session.commit()
            return 'success: Created a course'
        except:
            return 'error: Enter the field values correctly'
