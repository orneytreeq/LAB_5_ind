from app import app
from flask import render_template, request
import constants
@app.route('/', methods=['GET'])
def index():


 n = request.values.get('n')
 if (not n):
 	n = 5

 html = render_template(
 'index.html',
 subject_list = constants.subjects,
 n = int(n),
 len = len
 )
 return html
