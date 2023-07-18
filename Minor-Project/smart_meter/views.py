from http.client import HTTPResponse
import requests
import json
import datetime
from dateutil.tz import*
import calendar
from django.contrib import messages
from smart_meter.models import Notification
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as log, logout


def login(request):
    return render(request, 'login.html')

def map(request):
    return render(request, 'map.html')

def contact(request):
    return render(request, 'contact.html')

def notification(request):
    if request.method == "POST":
        customer_notification = request.POST.get('customer_notification')
        Notification(user_notice = customer_notification).save()
    return redirect('/admin')
    
def changepw(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        user = User.objects.get(id = request.user.id)
        password1 = request.POST.get('new_password1')
        password2 = request.POST.get('new_password2')
        check = user.check_password(old_password)

        if (password1 == password2 and check ==True):
            user.set_password(password1)
            user.save()
            messages.success(request, 'Password Changed sucessfully, Login with new password')

        else:
            messages.success(request, 'Invalid data Please try again')
        
    return redirect('/index')




def index(request):
    if request.user.is_anonymous:
        return redirect('/')

    response1 = requests.get(
        'https://api.thingspeak.com/channels/1650274/feeds.json?api_key=RFX5OCDEA14IIK6S&timezone=Asia%2FKathmandu&results=1')
    res1 = json.loads(response1.text)
    channel = res1['channel']['last_entry_id']

    response2 = requests.get(
        f"https://api.thingspeak.com/channels/1650274/feeds.json?api_key=RFX5OCDEA14IIK6S&timezone=Asia%2FKathmandu&results={channel}")
    res2 = json.loads(response2.text)['feeds']
    
    taken_year = int(res1['channel']['created_at'][0:4])
    january_set = set()
    february_set = set()
    march_set = set()
    april_set = set()
    may_set = set()
    june_set = set()
    july_set = set()
    august_set = set()
    september_set = set()
    october_set = set()
    november_set = set()
    december_set = set()

    set1 = set()
    set2 = set()
    set3 = set()
    set4 = set()
    set5 = set()
    set6 = set()
    set7 = set()
    set8 = set()
    set9 = set()
    set10 = set()
    set11 = set()
    set12 = set()
    set13 = set()
    set14 = set()
    set15 = set()
    set16 = set()
    set17 = set()
    set18 = set()
    set19 = set()
    set20 = set()
    set21 = set()
    set22 = set()
    set23 = set()
    set24 = set()
    set25 = set()
    set26 = set()
    set27 = set()
    set28 = set()
    set29 = set()
    set30 = set()
    set_month = set()
    set_month_reference = set()
    set_day_reference = set()

    list1h = sorted([])
    list2h = sorted([])
    list3h = sorted([])
    list4h = sorted([])
    list5h = sorted([])
    list6h = sorted([])
    list7h = sorted([])
    list8h = sorted([])
    list9h = sorted([])
    list10h = sorted([])
    list11h = sorted([])
    list12h = sorted([])
    list13h = sorted([])
    list14h = sorted([])
    list15h = sorted([])
    list16h = sorted([])
    list17h = sorted([])
    list18h = sorted([])
    list19h = sorted([])
    list20h = sorted([])
    list21h = sorted([])
    list22h = sorted([])
    list23h = sorted([])
    list24h = sorted([])
    list_day = sorted([])
    list_hour_reference = sorted([])
    for raw_data in res2:
        raw_date = raw_data['created_at']
        year = raw_date[0:4]
        month = raw_date[5:7]
        day = raw_date[8:10]
        hour = raw_date[11:13]
        minute = raw_date[14:16]
        datetime_object = datetime.datetime.strptime(
            f'{year} {month} {day} {hour}:{minute}', '%Y %m %d %H:%M')
        if (datetime_object.date().year <= datetime.datetime.now(tzoffset('GMT',20700)).year):
            grand_total = float(raw_data['field1'])
            
        if (datetime_object.date().year == taken_year + 0):
            taken_year_unit0 = float(raw_data['field1'])
        else:
            taken_year_unit0 = 0            

        if (datetime_object.date().year == taken_year + 1):
            taken_year_unit1 = float(raw_data['field1'])
        else:
            taken_year_unit1 = 0
        if (datetime_object.date().year == taken_year + 2):
            taken_year_unit2 = float(raw_data['field1'])
        else:
            taken_year_unit2 = 0
        if (datetime_object.date().year == taken_year + 3):
            taken_year_unit3 = float(raw_data['field1'])
        else:
            taken_year_unit3 = 0
        if (datetime_object.date().year == taken_year + 4):
            taken_year_unit4 = float(raw_data['field1'])
        else:
            taken_year_unit4 = 0
        if (datetime_object.date().year == taken_year + 5):
            taken_year_unit5 = float(raw_data['field1'])
        else:
            taken_year_unit5 = 0
        if (datetime_object.date().year == taken_year + 6):
            taken_year_unit6 = float(raw_data['field1'])
        else:
            taken_year_unit6 = 0
        if (datetime_object.date().year == taken_year + 7):
            taken_year_unit7 = float(raw_data['field1'])
        else:
            taken_year_unit7 = 0
        if (datetime_object.date().year == taken_year + 8):
            taken_year_unit8 = float(raw_data['field1'])
        else:
            taken_year_unit8 = 0
        if (datetime_object.date().year == taken_year + 9):
            taken_year_unit9 = float(raw_data['field1'])
        else:
            taken_year_unit9 = 0
        if (datetime_object.date().year == taken_year + 10):
            taken_year+=10

        if (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year):
            this_year_total = float(raw_data['field1'])

        if (datetime_object.date().month == 1 and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            january = float(raw_data['field1'])
            january_set.add(january)

        if (datetime_object.date().month == 2 and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            february = float(raw_data['field1'])
            february_set.add(february)

        if (datetime_object.date().month == 3 and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            march = float(raw_data['field1'])
            march_set.add(march)

        if (datetime_object.date().month == 4 and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            april = float(raw_data['field1'])
            april_set.add(april)

        if (datetime_object.date().month == 5 and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            may = float(raw_data['field1'])
            may_set.add(may)

        if (datetime_object.date().month == 6 and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            june = float(raw_data['field1'])
            june_set.add(june)

        if (datetime_object.date().month == 7 and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            july = float(raw_data['field1'])
            july_set.add(july)

        if (datetime_object.date().month == 8 and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            august = float(raw_data['field1'])
            august_set.add(august)

        if (datetime_object.date().month == 9 and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            september = float(raw_data['field1'])
            september_set.add(september)

        if (datetime_object.date().month == 10 and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            october = float(raw_data['field1'])
            october_set.add(october)

        if (datetime_object.date().month == 11 and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            november = float(raw_data['field1'])
            november_set.add(november)

        if (datetime_object.date().month == 12 and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            december = float(raw_data['field1'])
            december_set.add(december)
            set_month_reference.add(december)
            january_set.clear()
            february_set.clear()
            march_set.clear()
            april_set.clear()
            may_set.clear()
            june_set.clear()
            july_set.clear()
            august_set.clear()
            september_set.clear()
            october_set.clear()
            november_set.clear()
            december_set.clear()

        if((0 < datetime_object.date().day <= 30) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            month_unit = round(float(raw_data['field1']), 2)
            set_month.add(month_unit)
            if (datetime.datetime.now().hour == 1):
                set_day_reference.clear()

        if((datetime_object.date().day == 1) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            one = float(raw_data['field1'])
            set1.add(one)

        if((datetime_object.date().day == 2) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            two = float(raw_data['field1'])
            set2.add(two)

        if((datetime_object.date().day == 3) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            three = float(raw_data['field1'])
            set3.add(three)

        if((datetime_object.date().day == 4) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            four = float(raw_data['field1'])
            set4.add(four)

        if((datetime_object.date().day == 5) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            five = float(raw_data['field1'])
            set5.add(five)

        if((datetime_object.date().day == 6) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            six = float(raw_data['field1'])
            set6.add(six)

        if((datetime_object.date().day == 7) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            seven = float(raw_data['field1'])
            set7.add(seven)

        if((datetime_object.date().day == 8) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            eight = float(raw_data['field1'])
            set8.add(eight)

        if((datetime_object.date().day == 9) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            nine = float(raw_data['field1'])
            set9.add(nine)

        if((datetime_object.date().day == 10) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            ten = float(raw_data['field1'])
            set10.add(ten)

        if((datetime_object.date().day == 11) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            one1 = float(raw_data['field1'])
            set11.add(one1)

        if((datetime_object.date().day == 12) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            one2 = float(raw_data['field1'])
            set12.add(one2)

        if((datetime_object.date().day == 13) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            one3 = float(raw_data['field1'])
            set13.add(one3)

        if((datetime_object.date().day == 14) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            one4 = float(raw_data['field1'])
            set14.add(one4)

        if((datetime_object.date().day == 15) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            one5 = float(raw_data['field1'])
            set15.add(one5)

        if((datetime_object.date().day == 16) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            one6 = float(raw_data['field1'])
            set16.add(one6)

        if((datetime_object.date().day == 17) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            one7 = float(raw_data['field1'])
            set17.add(one7)

        if((datetime_object.date().day == 18) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            one8 = float(raw_data['field1'])
            set18.add(one8)

        if((datetime_object.date().day == 19) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            one9 = float(raw_data['field1'])
            set19.add(one9)

        if((datetime_object.date().day == 20) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            two0 = float(raw_data['field1'])
            set20.add(two0)

        if((datetime_object.date().day == 21) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            two1 = float(raw_data['field1'])
            set21.add(two1)

        if((datetime_object.date().day == 22) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            two2 = float(raw_data['field1'])
            set22.add(two2)

        if((datetime_object.date().day == 23) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            two3 = float(raw_data['field1'])
            set23.add(two3)

        if((datetime_object.date().day == 24) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            two4 = float(raw_data['field1'])
            set24.add(two4)

        if((datetime_object.date().day == 25) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            two5 = float(raw_data['field1'])
            set25.add(two5)

        if((datetime_object.date().day == 26) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            two6 = float(raw_data['field1'])
            set26.add(two6)

        if((datetime_object.date().day == 27) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            two7 = float(raw_data['field1'])
            set27.add(two7)

        if((datetime_object.date().day == 28) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            two8 = float(raw_data['field1'])
            set28.add(two8)

        if((datetime_object.date().day == 29) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            two9 = float(raw_data['field1'])
            set29.add(two9)

        if((datetime_object.date().day == 30) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            three0 = float(raw_data['field1'])
            set30.add(three0)

        if((datetime_object.date().day == list(calendar.monthrange(datetime_object.date().year, datetime_object.date().month))[1]) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            set_day_reference.add(float(raw_data['field1']))
            set1.clear()
            set2.clear()
            set3.clear()
            set4.clear()
            set5.clear()
            set6.clear()
            set7.clear()
            set8.clear()
            set9.clear()
            set10.clear()
            set11.clear()
            set12.clear()
            set13.clear()
            set14.clear()
            set15.clear()
            set16.clear()
            set17.clear()
            set18.clear()
            set19.clear()
            set20.clear()
            set21.clear()
            set22.clear()
            set23.clear()
            set24.clear()
            set25.clear()
            set26.clear()
            set27.clear()
            set28.clear()
            set29.clear()
            set30.clear()
        if ((datetime_object.time().hour == 1) and (datetime_object.date().day == datetime.datetime.now(tzoffset('GMT', 20700)).day) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            oneh = float(raw_data['field1'])
            list1h.append(oneh)

        if ((datetime_object.time().hour == 2) and (datetime_object.date().day == datetime.datetime.now(tzoffset('GMT', 20700)).day) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            twoh = float(raw_data['field1'])
            list2h.append(twoh)
            list_hour_reference.clear()

        if ((datetime_object.time().hour == 3) and (datetime_object.date().day == datetime.datetime.now(tzoffset('GMT', 20700)).day) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            threeh = float(raw_data['field1'])
            list3h.append(threeh)

        if ((datetime_object.time().hour == 4) and (datetime_object.date().day == datetime.datetime.now(tzoffset('GMT', 20700)).day) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            fourh = float(raw_data['field1'])
            list4h.append(fourh)

        if ((datetime_object.time().hour == 5) and (datetime_object.date().day == datetime.datetime.now(tzoffset('GMT', 20700)).day) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            fiveh = float(raw_data['field1'])
            list5h.append(fiveh)

        if ((datetime_object.time().hour == 6) and (datetime_object.date().day == datetime.datetime.now(tzoffset('GMT', 20700)).day) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            sixh = float(raw_data['field1'])
            list6h.append(sixh)

        if ((datetime_object.time().hour == 7) and (datetime_object.date().day == datetime.datetime.now(tzoffset('GMT', 20700)).day) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            sevenh = float(raw_data['field1'])
            list7h.append(sevenh)

        if ((datetime_object.time().hour == 8) and (datetime_object.date().day == datetime.datetime.now(tzoffset('GMT', 20700)).day) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            eighth = float(raw_data['field1'])
            list8h.append(eighth)

        if ((datetime_object.time().hour == 9) and (datetime_object.date().day == datetime.datetime.now(tzoffset('GMT', 20700)).day) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            nineh = float(raw_data['field1'])
            list9h.append(nineh)

        if ((datetime_object.time().hour == 10) and (datetime_object.date().day == datetime.datetime.now(tzoffset('GMT', 20700)).day) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            tenh = float(raw_data['field1'])
            list10h.append(tenh)

        if ((datetime_object.time().hour == 11) and (datetime_object.date().day == datetime.datetime.now(tzoffset('GMT', 20700)).day) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            one1h = float(raw_data['field1'])
            list11h.append(one1h)

        if ((datetime_object.time().hour == 12) and (datetime_object.date().day == datetime.datetime.now(tzoffset('GMT', 20700)).day) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            one2h = float(raw_data['field1'])
            list12h.append(one2h)


        if ((datetime_object.time().hour == 13) and (datetime_object.date().day == datetime.datetime.now(tzoffset('GMT', 20700)).day) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            one3h = float(raw_data['field1'])
            list13h.append(one3h)

        if ((datetime_object.time().hour == 14) and (datetime_object.date().day == datetime.datetime.now(tzoffset('GMT', 20700)).day) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            one4h = float(raw_data['field1'])
            list14h.append(one4h)

        if ((datetime_object.time().hour == 15) and (datetime_object.date().day == datetime.datetime.now(tzoffset('GMT', 20700)).day) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            one5h = float(raw_data['field1'])
            list15h.append(one5h)

        if ((datetime_object.time().hour == 16) and (datetime_object.date().day == datetime.datetime.now(tzoffset('GMT', 20700)).day) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            one6h = float(raw_data['field1'])
            list16h.append(one6h)

        if ((datetime_object.time().hour == 17) and (datetime_object.date().day == datetime.datetime.now(tzoffset('GMT', 20700)).day) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            one7h = float(raw_data['field1'])
            list17h.append(one7h)

        if ((datetime_object.time().hour == 18) and (datetime_object.date().day == datetime.datetime.now(tzoffset('GMT', 20700)).day) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            one8h = float(raw_data['field1'])
            list18h.append(one8h)

        if ((datetime_object.time().hour == 19) and (datetime_object.date().day == datetime.datetime.now(tzoffset('GMT', 20700)).day) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            one9h = float(raw_data['field1'])
            list19h.append(one9h)

        if ((datetime_object.time().hour == 20) and (datetime_object.date().day == datetime.datetime.now(tzoffset('GMT', 20700)).day) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            two0h = float(raw_data['field1'])
            list20h.append(two0h)

        if ((datetime_object.time().hour == 21) and (datetime_object.date().day == datetime.datetime.now(tzoffset('GMT', 20700)).day) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            two1h = float(raw_data['field1'])
            list21h.append(two1h)

        if ((datetime_object.time().hour == 22) and (datetime_object.date().day == datetime.datetime.now(tzoffset('GMT', 20700)).day) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            two2h = float(raw_data['field1'])
            list22h.append(two2h)

        if ((datetime_object.time().hour == 23) and (datetime_object.date().day == datetime.datetime.now(tzoffset('GMT', 20700)).day) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            two3h = float(raw_data['field1'])
            list23h.append(two3h)

        if ((datetime_object.time().hour == 00) and (datetime_object.date().day == datetime.datetime.now(tzoffset('GMT', 20700)).day) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            two4h = float(raw_data['field1'])
            list24h.append(two4h)
            list_hour_reference.append(two4h)
            list1h.clear()
            list2h.clear()
            list3h.clear()
            list4h.clear()
            list5h.clear()
            list6h.clear()
            list7h.clear()
            list8h.clear()
            list9h.clear()
            list10h.clear()
            list11h.clear()
            list12h.clear()
            list13h.clear()
            list14h.clear()
            list15h.clear()
            list16h.clear()
            list17h.clear()
            list18h.clear()
            list19h.clear()
            list20h.clear()
            list21h.clear()
            list22h.clear()
            list23h.clear()
            list24h.clear()
        if ((00 <= datetime_object.time().hour <= 23) and (datetime_object.date().day == datetime.datetime.now(tzoffset('GMT', 20700)).day) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
            day_unit = float(raw_data['field1'])
            list_day.append(day_unit)

    january_list = sorted(list(january_set))
    february_list = sorted(list(february_set))
    march_list = sorted(list(march_set))
    april_list = sorted(list(april_set))
    may_list = sorted(list(may_set))
    june_list = sorted(list(june_set))
    july_list = sorted(list(july_set))
    august_list = sorted(list(august_set))
    september_list = sorted(list(september_set))
    october_list = sorted(list(october_set))
    november_list = sorted(list(november_set))
    december_list = sorted(list(december_set))

    list1 = sorted(list(set1))
    list2 = sorted(list(set2))
    list3 = sorted(list(set3))
    list4 = sorted(list(set4))
    list5 = sorted(list(set5))
    list6 = sorted(list(set6))
    list7 = sorted(list(set7))
    list8 = sorted(list(set8))
    list9 = sorted(list(set9))
    list10 = sorted(list(set10))
    list11 = sorted(list(set11))
    list12 = sorted(list(set12))
    list13 = sorted(list(set13))
    list14 = sorted(list(set14))
    list15 = sorted(list(set15))
    list16 = sorted(list(set16))
    list17 = sorted(list(set17))
    list18 = sorted(list(set18))
    list19 = sorted(list(set19))
    list20 = sorted(list(set20))
    list21 = sorted(list(set21))
    list22 = sorted(list(set22))
    list23 = sorted(list(set23))
    list24 = sorted(list(set24))
    list25 = sorted(list(set25))
    list26 = sorted(list(set26))
    list27 = sorted(list(set27))
    list28 = sorted(list(set28))
    list29 = sorted(list(set29))
    list30 = sorted(list(set30))
    list_month = sorted(list(set_month))
    list_month_reference = sorted(list(set_month_reference))
    list_day_reference = sorted(list(set_day_reference))

    if january_list:
        if list_day_reference:
            january_units = january_list[len(january_list)-1] - list_day_reference[len(list_day_reference) -1]
        else:
            january_units = january_list[len(january_list)-1] - january_list[0]
    else:
        january_units = 0

    if february_list:
        if january_list:
            february_units = february_list[len(february_list)-1] - january_list[len(january_list) -1]
        else:
            february_units = february_list[len(february_list)-1] - february_list[0]   
    else:
        february_units = 0

    if march_list:
        if february_list:
            march_units = march_list[len(march_list)-1] - february_list[len(february_list) -1]
        else:
            march_units = march_list[len(march_list)-1] - march_list[0]  
    else:
        march_units = 0

    if april_list:
        if march_list:
            april_units = april_list[len(april_list)-1] - march_list[len(march_list)-1]
        else:
            april_units = april_list[len(april_list)-1] - april_list[0]    
    else:
        april_units = 0

    if may_list:
        if april_list:
            may_units = may_list[len(may_list)-1] - april_list[len(april_list)-1]
        else:
            april_units = april_list[len(april_list)-1] - april_list[0]
    else:
        may_units = 0

    if june_list:
        if may_list:
            june_units = june_list[len(june_list)-1] - may_list[len(may_list)-1]
        else:
            june_units = june_list[len(june_list)-1] - june_list[0]    
    else:
        june_units = 0

    if july_list:
        if june_list:
            july_units = july_list[len(july_list)-1] - june_list[len(june_list)-1]
        else:
            july_units = july_list[len(july_list)-1] - july_list[0]
    else:
        july_units = 0

    if august_list:
        if july_list:
            august_units = august_list[len(august_list)-1] - july_list[len(july_list) -1]
        else:
            august_units = august_list[len(august_list)-1] - august_list[0]
    else:
        august_units = 0

    if september_list:
        if august_list:
            september_units = september_list[len(september_list)-1] - august_list[len(august_list)-1]
        else:
            september_units = september_list[len(september_list)-1] - september_list[0]
    else:
        september_units = 0

    if october_list:
        if september_list:
            october_units = october_list[len(october_list)-1] - september_list[len(september_list)-1]
        else:
            october_units = october_list[len(october_list)-1] - october_list[0]
    else:
        october_units = 0

    if november_list:
        if october_list:
            november_units = november_list[len(november_list)-1] - october_list[len(october_list) -1]
        else:
            november_units = november_list[len(november_list)-1] - november_list[0]
    else:
        november_units = 0

    if december_list:
        if november_list:
            december_units = december_list[len(december_list)-1] - november_list[len(november_list) -1]
        else:
            december_units = december_list[len(december_list)-1] - december_list[0]
    else:
        december_units = 0

    if list1:
        if list_hour_reference:
            unit_1 = list1[len(list1)-1] - list_hour_reference[len(list_hour_reference)-1]
        else:
            unit_1 = list1[len(list1)-1] - list1[0]

    else:
        unit_1 = 0
    if list2:
        if list1:
            unit_2 = list2[len(list2)-1] - list1[len(list1)-1]
        else:
            unit_2 = list2[len(list2)-1] - list2[0]

    else:
        unit_2 = 0
    if list3:
        if list2:
            unit_3 = list3[len(list3)-1] - list2[len(list2)-1]
        else:
            unit_3 = list3[len(list3)-1] - list3[0]

    else:
        unit_3 = 0
    if list4:
        if list3:
            unit_4 = list4[len(list4)-1] - list3[len(list3)-1]
        else:
            unit_4 = list4[len(list4)-1] - list4[0]

    else:
        unit_4 = 0
    if list5:
        if list4:
            unit_5 = list5[len(list5)-1] - list4[len(list4)-1]
        else:
            unit_5 = list5[len(list5)-1] - list5[0]

    else:
        unit_5 = 0
    if list6:
        if list5:
            unit_6 = list6[len(list6)-1] - list5[len(list5)-1]
        else:
            unit_6 = list6[len(list6)-1] - list6[0]

    else:
        unit_6 = 0
    if list7:
        if list6:
            unit_7 = list7[len(list7)-1] - list6[len(list6)-1]
        else:
            unit_7 = list7[len(list7)-1] - list7[0]

    else:
        unit_7 = 0
    if list8:
        if list7:
            unit_8 = list8[len(list8)-1] - list7[len(list7)-1]
        else:
            unit_8 = list8[len(list8)-1] - list8[0]

    else:
        unit_8 = 0
    if list9:
        if list8:
            unit_9 = list9[len(list9)-1] - list8[len(list8)-1]
        else:
            unit_9 = list9[len(list9)-1] - list9[0]
    else:
        unit_9 = 0
    if list10:
        if list9:
            unit_10 = list10[len(list10)-1] - list9[len(list9)-1]
        else:
            unit_10 - list10[len(list10)-1] - list10[0]
    else:
        unit_10 = 0
    if list11:
        if list10:
            unit_11 = list11[len(list11)-1] - list10[len(list10)-1]
        else:
            unit_11 - list11[len(list11)-1] - list11[0]
    else:
        unit_11 = 0
    if list12:
        if list11:
            unit_12 = list12[len(list12)-1] - list11[len(list11)-1]
        else:
            unit_12 - list12[len(list12)-1] - list12[0]
    else:
        unit_12 = 0
    if list13:
        if list12:
            unit_13 = list13[len(list13)-1] - list12[len(list12)-1]
        else:
            unit_13 - list13[len(list13)-1] - list13[0]
    else:
        unit_13 = 0
    if list14:
        if list13:
            unit_14 = list14[len(list14)-1] - list13[len(list13)-1]
        else:
            unit_14 = list14[len(list14)-1] - list14[0]
    else:
        unit_14 = 0
    if list15:
        if list14:
            unit_15 = list15[len(list15)-1] - list14[len(list14)-1]
        else:
            unit_15 = list15[len(list15)-1] - list15[0]
    else:
        unit_15 = 0
    if list16:
        if list15:
            unit_16 = list16[len(list16)-1] - list15[len(list15)-1]
        else:
            unit_16 = list16[len(list16)-1] - list16[0]
    else:
        unit_16 = 0
    if list17:
        if list16:
            unit_17 = list17[len(list17)-1] - list16[len(list16)-1]
        else:
            unit_17 = list17[len(list17)-1] - list17[0]
    else:
        unit_17 = 0
    if list18:
        if list17:
            unit_18 = list18[len(list18)-1] - list17[len(list17)-1]
        else:
            unit_18 = list18[len(list18)-1] - list18[0]
    else:
        unit_18 = 0

    if list19:
        if list18:
            unit_19 = list19[len(list19)-1] - list18[len(list18)-1]
        else:
            unit_19 = list19[len(list19)-1] - list19[0]
    else:
        unit_19 = 0

    if list20:
        if list19:
            unit_20 = list20[len(list20)-1] - list19[len(list19)-1]
        else:
            unit_20 = list20[len(list20)-1] - list20[0]
    else:
        unit_20 = 0
    if list21:
        if list20:
            unit_21 = list21[len(list21)-1] - list20[len(list20)-1]
        else:
            unit_21 = list21[len(list21)-1] - list21[0]
    else:
        unit_21 = 0

    if list22:
        if list20:
            unit_22 = list22[len(list22)-1] - list21[len(list21)-1]
        else:
            unit_22 = list22[len(list22)-1] - list22[0]
    else:
        unit_22 = 0
    if list23:
        if list22:
            unit_23 = list23[len(list23)-1] - list22[len(list22)-1]
        else:
            unit_23 = list23[len(list23)-1] - list23[0]
    else:
        unit_23 = 0
    if list24:
        if list23:
            unit_24 = list24[len(list24)-1] - list23[len(list23)-1]
        else:
            unit_24 = list24[len(list24)-1] - list24[0]
    else:
        unit_24 = 0
    if list25:
        if list24:
            unit_25 = list25[len(list25)-1] - list24[len(list24)-1]
        else:
            unit_25 = list25[len(list25)-1] - list25[0]
    else:
        unit_25 = 0
    if list26:
        if list25:
            unit_26 = list26[len(list26)-1] - list25[len(list25)-1]
        else:
            unit_26 = list26[len(list26)-1] - list26[0]
    else:
        unit_26 = 0
    if list27:
        if list26:
            unit_27 = list27[len(list27)-1] - list26[len(list26)-1]
        else:
            unit_27 = list27[len(list27)-1] - list27[0]
    else:
        unit_27 = 0

    if list28:
        if list27:
            unit_28 = list28[len(list28)-1] - list27[len(list27)-1]
        else:
            unit_28 = list28[len(list28)-1] - list28[0]
    else:
        unit_28 = 0
    if list29:
        if list28:
            unit_29 = list29[len(list29)-1] - list28[len(list28)-1]
        else:
            unit_29 = list29[len(list29)-1] - list29[0]
    else:
        unit_29 = 0
    if list30:
        if list29:
            unit_30 = list30[len(list30)-1] - list29[len(list29)-1]
        else:
            unit_30 = list30[len(list30)-1] - list30[0]
    else:
        unit_30 = 0
    if list_month:
        month_unit = list_month[len(list_month)-1] - list_month[0]
    else:
        month_unit = 0

    if list1h:
        if list_hour_reference:
            unit_1h = list1h[len(list1h)-1] - list_hour_reference[len(list_hour_reference)-1]
        else:
            unit_1h = list1h[len(list1h)-1] - list1h[0]    
    else:
        unit_1h = 0

    if list2h:
        if list1h:
            unit_2h = list2h[len(list2h)-1] - list1h[len(list1h)-1]
        else:
            unit_2h = list2h[len(list2h)-1] - list2h[0]
    else:
        unit_2h = 0

    if list3h:
        if list2h:
            unit_3h = list2h[len(list3h)-1] - list2h[len(list2h)-1]
        else:
            unit_3h = list3h[len(list3h)-1] - list3h[0]
    else:
        unit_3h = 0

    if list4h:
        if list3h:
            unit_4h = list4h[len(list4h)-1] - list3h[len(list3h)-1]
        else:
            unit_4h = list4h[len(list4h)-1] - list4h[0]
    else:
        unit_4h = 0

    if list5h:
        if list5h:
            unit_5h = list5h[len(list5h)-1] - list5h[len(list4h)-1]
        else:
            unit_5h = list5h[len(list5h)-1] - list5h[0]
    else:
        unit_5h = 0

    if list6h:
        if list5h:
            unit_6h = list6h[len(list6h)-1] - list5h[len(list5h)-1]
        else:
            unit_6h = list6h[len(list6h)-1] - list6h[0]
    else:
        unit_6h = 0

    if list7h:
        if list6h:
            unit_7h = list7h[len(list7h)-1] - list6h[len(list6h)-1]
        else:
            unit_7h = list7h[len(list7h)-1] - list7h[0]
    else:
        unit_7h = 0

    if list8h:
        if list7h:
            unit_8h = list8h[len(list8h)-1] - list7h[len(list7h) - 1]
        else:
            unit_8h = list8h[len(list8h)-1] - list8h[0]    
    else:
        unit_8h = 0

    if list9h:
        if list8h:
            unit_9h = list9h[len(list9h)-1] - list8h[len(list8h) - 1]
        else:
            unit_9h = list9h[len(list9h)-1] - list9h[0]
    else:
        unit_9h = 0

    if list10h:
        if list9h:
            unit_10h = list10h[len(list10h)-1] - list9h[len(list9h) - 1]
        else:
            unit_10h = list10h[len(list10h)-1] - list10h[0]
    else:
        unit_10h = 0

    if list11h:
        if list10h:
            unit_11h = list11h[len(list11h)-1] - list10h[len(list10h)-1]
        else:
            unit_11h = list11h[len(list11h)-1] - list11h[0]    
    else:
        unit_11h = 0

    if list12h:
        if list11h:
            unit_12h = list12h[len(list12h)-1] - list11h[len(list11h) - 1]
        else:
            unit_12h = list12h[len(list12h)-1] - list12h[0] 
    else:
        unit_12h = 0

    if list13h:
        if list12h:
            unit_13h = list13h[len(list13h)-1] - list12h[len(list12h) - 1]
        else:
            unit_13h = list13h[len(list13h)-1] - list13h[0]    
    else:
        unit_13h = 0

    if list14h:
        if list13h:
            unit_14h = list14h[len(list14h)-1] - list13h[len(list13h) - 1]
        else:
            unit_14h = list14h[len(list14h)-1] - list14h[0] 
    else:
        unit_14h = 0

    if list15h:
        if list14h:
            unit_15h = list15h[len(list15h)-1] - list14h[len(list14h) - 1]
        else:
            unit_15h = list15h[len(list15h)-1] - list15h[0]
    else:
        unit_15h = 0

    if list16h:
        if list15h:
            unit_16h = list16h[len(list16h)-1] - list15h[len(list15h) - 1]
        else:
            unit_16h = list16h[len(list16h)-1] - list16h[0]
    else:
        unit_16h = 0

    if list17h:
        if list16h:
            unit_17h = list17h[len(list17h)-1] - list16h[len(list16h) - 1]
        else:
            unit_17h = list17h[len(list17h)-1] - list17h[0]
    else:
        unit_17h = 0

    if list18h:
        if list17h:
            unit_18h = list18h[len(list18h)-1] - list17h[len(list17h) - 1]
        else:
            unit_18h = list18h[len(list18h)-1] - list18h[0]   
    else:
        unit_18h = 0

    if list19h:
        if list18h:
            unit_19h = list19h[len(list19h)-1] - list18h[len(list18h) - 1]
        else:
            unit_19h = list19h[len(list19h)-1] - list19h[0]
    else:
        unit_19h = 0

    if list20h:
        if list19h:
            unit_20h = list20h[len(list20h)-1] - list19h[len(list19h) - 1]
        else:
            unit_20h = list20h[len(list20h)-1] - list20h[0] 
    else:
        unit_20h = 0

    if list21h:
        if list20h:
            unit_21h = list21h[len(list21h)-1] - list20h[len(list20h) - 1]
        else:
            unit_21h = list21h[len(list21h)-1] - list21h[0]
    else:
        unit_21h = 0

    if list22h:
        if list21h:
            unit_22h = list22h[len(list22h)-1] - list21h[len(list21h) - 1]
        else:
            unit_22h = list22h[len(list22h)-1] - list22h[0] 
    else:
        unit_22h = 0

    if list23h:
        if list22h:
            unit_23h = list23h[len(list23h)-1] - list22h[len(list22h) - 1]
        else:
            unit_23h = list23h[len(list23h)-1] - list23h[0]    
    else:
        unit_23h = 0

    if list24h:
        if list23h:
            unit_24h = list24h[len(list24h)-1] - list23h[len(list23h) - 1]
        else:
            unit_24h = list24h[len(list24h)-1] - list24h[0]    
    else:
        unit_24h = 0

    if list_day:
        day_total = round(list_day[len(list_day)-1] - list_day[0], 2)
    else:
        day_total = 0


    user_notice = Notification.objects.all()
    unit_consumption = {
        'JAN': january_units,
        'FEB': february_units,
        'MAR': march_units,
        'APR': april_units,
        'MAY': may_units,
        'JUNE': june_units,
        'JULY': july_units,
        'AUG': august_units,
        'SEPT': september_units,
        'OCT': october_units,
        'NOV': november_units,
        'DEC': december_units,
        "YEAR_TOTAL": round(this_year_total,2),
        "YEAR_TOTAL_COST": round(this_year_total*12, 2),
        "unit_1": unit_1,
        "unit_2": unit_2,
        "unit_3": unit_3,
        "unit_4": unit_4,
        "unit_5": unit_5,
        "unit_6": unit_6,
        "unit_7": unit_7,
        "unit_8": unit_8,
        "unit_9": unit_9,
        "unit_10": unit_10,
        "unit_11": unit_11,
        "unit_12": unit_12,
        "unit_13": unit_13,
        "unit_14": unit_14,
        "unit_15": unit_15,
        "unit_16": unit_16,
        "unit_17": unit_17,
        "unit_18": unit_18,
        "unit_19": unit_19,
        "unit_20": unit_20,
        "unit_21": unit_21,
        "unit_22": unit_22,
        "unit_23": unit_23,
        "unit_24": unit_24,
        "unit_25": unit_25,
        "unit_26": unit_26,
        "unit_27": unit_27,
        "unit_28": unit_28,
        "unit_29": unit_29,
        "unit_30": unit_30,
        "MONTH_TOTAL": round(month_unit,2),
        "MONTH_TOTAL_COST": round(month_unit*12, 2),
        "unit_1h": unit_1h,
        "unit_2h": unit_2h,
        "unit_3h": unit_3h,
        "unit_4h": unit_4h,
        "unit_5h": unit_5h,
        "unit_6h": unit_6h,
        "unit_7h": unit_7h,
        "unit_8h": unit_8h,
        "unit_9h": unit_9h,
        "unit_10h": unit_10h,
        "unit_11h": unit_11h,
        "unit_12h": unit_12h,
        "unit_13h": unit_13h,
        "unit_14h": unit_14h,
        "unit_15h": unit_15h,
        "unit_16h": unit_16h,
        "unit_17h": unit_17h,
        "unit_18h": unit_18h,
        "unit_19h": unit_19h,
        "unit_20h": unit_20h,
        "unit_21h": unit_21h,
        "unit_22h": unit_22h,
        "unit_23h": unit_23h,
        "unit_24h": unit_24h,
        "DAY_TOTAL": day_total,
        "DAY_TOTAL_COST": round(day_total*12, 2),
        "year0":taken_year_unit0,
        "year1":taken_year_unit1,
        "year2":taken_year_unit2,
        "year3":taken_year_unit3,
        "year4":taken_year_unit4,
        "year5":taken_year_unit5,
        "year6":taken_year_unit6,
        "year7":taken_year_unit7,
        "year8":taken_year_unit8,
        "year9":taken_year_unit9,
        "year_label0":taken_year + 0,
        "year_label1":taken_year + 1,
        "year_label2":taken_year + 2,
        "year_label3":taken_year + 3,
        "year_label4":taken_year + 4,
        "year_label5":taken_year + 5,
        "year_label6":taken_year + 6,
        "year_label7":taken_year + 7,
        "year_label8":taken_year + 8,
        "year_label9":taken_year + 9,
        "grand_total":round(grand_total,2),
        "grand_total_cost":round(grand_total*12,2),
        "user_notice":user_notice,
    }
    return render(request, 'index.html', unit_consumption)


def admin(request):
    if request.user.is_anonymous:
        return redirect('/')
    if request.user.is_superuser:
        response1 = requests.get(
            'https://api.thingspeak.com/channels/1650274/feeds.json?api_key=RFX5OCDEA14IIK6S&timezone=Asia%2FKathmandu&results=1')
        res1 = json.loads(response1.text)
        channel = res1['channel']['last_entry_id']

        response2 = requests.get(
            f"https://api.thingspeak.com/channels/1650274/feeds.json?api_key=RFX5OCDEA14IIK6S&timezone=Asia%2FKathmandu&results={channel}")
        res2 = json.loads(response2.text)['feeds']

        list_day = []
        set_month = set()
        for raw_data in res2:
            raw_date = raw_data['created_at']
            year = raw_date[0:4]
            month = raw_date[5:7]
            day = raw_date[8:10]
            hour = raw_date[11:13]
            minute = raw_date[14:16]
            datetime_object = datetime.datetime.strptime(
                f'{year} {month} {day} {hour}:{minute}', '%Y %m %d %H:%M')

            if (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year):
                this_year_total = float(raw_data['field1'])

            if ((00 <= datetime_object.time().hour <= 23) and (datetime_object.date().day == datetime.datetime.now(tzoffset('GMT', 20700)).day) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
                day_unit = float(raw_data['field1'])
                list_day.append(day_unit)

            if((0 < datetime_object.date().day <= 30) and (datetime_object.date().month == datetime.datetime.now(tzoffset('GMT', 20700)).month) and (datetime_object.date().year == datetime.datetime.now(tzoffset('GMT', 20700)).year)):
                month_unit = round(float(raw_data['field1']), 2)
                set_month.add(month_unit)

            list_month= sorted(list(set_month))
            if list_day:
                day_total = list_day[len(list_day)-1] - list_day[0]
            else:
                day_total = 0
            if list_month:
                month_unit = list_month[len(list_month)-1] - list_month[0]
            else:
                month_unit = 0

        clients = []
        for user in User.objects.all():
            clients.append(user.username)
        clients.remove(request.user.username)
        client_users  = {
            "client_users":clients,
            "DAY_TOTAL": round(day_total,2),
            "MONTH_TOTAL": round(month_unit,2),
            "YEAR_TOTAL": round(this_year_total,2),
        }
        return render(request, 'admin.html',client_users)
    else:
        return redirect('/index')


def user_login(request):
    if request.method == "POST":
        userid = request.POST.get('login_id')
        password = request.POST.get('login_password')

        user = authenticate(username=userid, password=password)
        if user is not None:
            if user.is_active:
                if user.is_superuser:
                    log(request, user)
                    return redirect('/admin')
                else:
                    log(request, user)
                    return redirect('/index')
            else:
                return redirect('/')
        else:
            return redirect('/')

    else:
        return redirect('/')


def app_logout(request):
    logout(request)
    return redirect('/')


def user_signup(request):
    if request.method == "POST":
        useid = request.POST.get('userid')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirm_password')

        if (password1 == password2):
            user = User.objects.create_user(username=useid, password=password1)
            user.save()
            messages.success(request, 'User created sucessfully')
            return redirect('/')
        else:
            messages.error(request, 'Password did not match please try again')
            return redirect("/")
    else:
        return redirect('/')

