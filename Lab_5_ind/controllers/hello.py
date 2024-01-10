#!/usr/bin/python

#- * -coding: utf - 8 - * -
from app import app
from flask import render_template, request
import constants
import numpy as np
#from sklearn.linear_model import LinearRegression

@ app.route('/', methods = ['GET'])
def hello():
    n = request.values.get('n')
    if not n:
        n = 5

    subject_id = request.values.getlist('subject[]')
    subjects_select = [constants.subjects[int(i)]
        for i in subject_id
    ]

    results = []

    data1 = request.values.getlist('data1[]')
    data1_int = [int(x) for x in data1]
    data2 = request.values.getlist('data2[]')
    data2_int = [int(x) for x in data2]

    print(subject_id)

    if request.values.get('remove') == 'true' or len(subjects_select) == 0 or '' in data1 or '' in data2:
        print('NO DATA')
        html = render_template('index.html',
            subject_list = constants.subjects,
            n = int(n),
            len = len)
        return html

    for el in subjects_select:
        if (el == 'коэффициент корреляции'):
            results.append([el, str(np.corrcoef(data1_int, data2_int))])
        elif(el == 'ковариация'):
            data1_np = np.array(data1_int)
            data2_np = np.array(data2_int)
            results.append([el, np.cov(data1_np, data2_np)[0, 1]])
        elif(el == 'линейная регрессия второго ряда на первый'):
            res = str(np.polyfit(data1_int, data2_int, 2))
            results.append([el, res])


    html = render_template('index.html',
        subject_list = constants.subjects,
        n = int(n),
        results = results,
        data1 = data1,
        data2 = data2,
        subject_id = subject_id,
        len = len)



    return html