from django.shortcuts import render
import psycopg2
import json
from django.http import HttpResponse
from .models import details, women

# Create your views here.


def index(request):
    return render(request, 'index.html')


def backend(request):
    if request.is_ajax() or request.method == 'POST':
        name = request.POST.get('name')
        father_name = request.POST.get('father_name')
        voter = request.POST.get('voter')
        door_no = request.POST.get('door_no')
        gender = request.POST.get('gender')
        status = request.POST.get('status')
        age = request.POST.get('age')
        mydb = psycopg2.connect(
            host='localhost', user='postgres', password='pavanyadav123', database='voterdb')
        mycursor = mydb.cursor()
        mysql = "select name from ward_ui_women where voter_id = %s"
        mycursor.execute(mysql, [voter])
        w = mycursor.fetchone()
        mysql = "select name from ward_ui_details where voter_id = %s"
        mycursor.execute(mysql, [voter])
        m = mycursor.fetchone()
        if status == 'married' and gender == 'female':
            if w or m:
                data = ['voter id already exists']
                return HttpResponse(json.dumps(data))
            else:
                data = 'insert into ward_ui_women(name,gender,age,husband_name,door_no,voter_id) values (%s,%s,%s,%s,%s,%s)'
                data2 = [name, gender, age, father_name, door_no, voter]
                mycursor.execute(data, data2)
                mydb.commit()
                data = {'name': '%s' % (name), 'father': '%s' % (father_name), 'age': '%s' % (age), 'gender': '%s' % (
                    gender), 'door_no': '%s' % (door_no), 'voter': '%s' % (voter), 'status': '%s' % (status)}
                return HttpResponse(json.dumps(data))
        else:
            if w or m:
                data = ['voter id already exists']
                return HttpResponse(json.dumps(data))
            else:
                data = 'insert into ward_ui_details(name,gender,age,father_name,door_no,voter_id) values (%s,%s,%s,%s,%s,%s)'
                data2 = [name, gender, age, father_name, door_no, voter]
                mycursor.execute(data, data2)
                mydb.commit()
                data = {'name': '%s' % (name), 'father': '%s' % (father_name), 'age': '%s' % (age), 'gender': '%s' % (
                    gender), 'door_no': '%s' % (door_no), 'voter': '%s' % (voter), 'status': '%s' % (status)}
                return HttpResponse(json.dumps(data))
    else:
        return HttpResponse('error')


def female(request):
    m = details.objects.all()
    w = women.objects.all()
    lm = len(m)
    lw = len(w)
    total = lm+lw
    return render(request, 'female.html', {'m': m, 'w': w,'total':total})


def find(request):
    mydb = psycopg2.connect(
        host='localhost', user='postgres', password='pavanyadav123', database='voterdb')
    mycursor = mydb.cursor()
    mycursor.execute("select gender from ward_ui_women")
    w = mycursor.fetchall()
    d = []
    for i in w:
        d.extend(i)
    w1 = len(d)
    mycursor.execute("select gender from ward_ui_details where gender = 'male'")
    m = mycursor.fetchall()
    d = []
    for j in m:
        d.extend(j)
    m1 = len(d)
    mycursor.execute(
        "select gender from ward_ui_details where gender = 'female'")
    f = mycursor.fetchall()
    d = []
    for k in f:
        d.extend(k)
    f1 = len(d)
    female = f1+w1
    return render(request, 'find.html', {'m1': m1,'female':female})

def search(request):
    if request.is_ajax() or request.method == 'post':
        data = request.POST.get('search')
        data = data+' '
        mydb = psycopg2.connect(host='localhost', user='postgres', password='pavanyadav123', database='voterdb')
        mycursor = mydb.cursor()
        if data.isalnum():
            m = "select * from ward_ui_details where voter_id =  %s"
            mycursor.execute(m,[data])
            w = mycursor.fetchall()
            if w:
                dat = w
                return HttpResponse(json.dumps(dat))
            else:
                m = "select * from ward_ui_women where voter_id =  %s"
                mycursor.execute(m, [data])
                w = mycursor.fetchall()
                if w:
                    dat = w
                    return HttpResponse(json.dumps(dat))
                else:
                    da = ['voter id not found in database']
                    return HttpResponse(json.dumps(da))
        else:
            m = "select name,father_name,age,gender,door_no,voter_id from ward_ui_details where name like  %s" % ("\'"+'%'+data+'%'+"\'")
            mycursor.execute(m)
            w = mycursor.fetchall()
            if w:
                m1 = "select name,husband_name,age,gender,door_no,voter_id from ward_ui_women where name like  %s" % ("\'"+'%'+data+'%'+"\'")
                mycursor.execute(m1)
                w1 = mycursor.fetchall()
                if w1:
                    dat = w + w1
                    return HttpResponse(json.dumps(dat))
                else:
                    dat = w
                    return HttpResponse(json.dumps(dat))
            else:
                m = "select name,husband_name,age,gender,door_no,voter_id from ward_ui_women where name like  %s" % ("\'"+'%'+data+'%'+"\'")
                mycursor.execute(m)
                w = mycursor.fetchall()
                if w:
                    dat = w
                    return HttpResponse(json.dumps(dat))
                else:
                    da = ['name not found in database']
                    return HttpResponse(json.dumps(da))
    else:
        return HttpResponse('error')

def total_male(request):
    if request.is_ajax():
        mydb = psycopg2.connect(
            host='localhost', user='postgres', password='pavanyadav123', database='voterdb')
        mycursor = mydb.cursor()
        mycursor.execute("select name,father_name,age,gender,door_no,voter_id from ward_ui_details where gender = 'male'")
        w = mycursor.fetchall()
        if w:
            return HttpResponse(json.dumps(w))
        else:
            return HttpResponse(json.dumps('No Data Exists'))
    else:
        return HttpResponse('error')
    

def total_female(request):
    if request.is_ajax():
        mydb = psycopg2.connect(
            host='localhost', user='postgres', password='pavanyadav123', database='voterdb')
        mycursor = mydb.cursor()
        mycursor.execute(
            "select name,father_name,age,gender,door_no,voter_id from ward_ui_details where gender = 'female'")
        w = mycursor.fetchall()
        if w:
            mycursor.execute(
                "select name,husband_name,age,gender,door_no,voter_id from ward_ui_women where gender = 'female'")
            w1 = mycursor.fetchall()
            if w1:
                dat = w + w1
                return HttpResponse(json.dumps(dat))
            else:
                dat = w
                return HttpResponse(json.dumps(dat))
        else:
            return HttpResponse('No Data Exists')
    else:
        return HttpResponse('error')
        
