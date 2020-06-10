from django.shortcuts import render
import datetime

def home(reguest):
    date = datetime.datetime.now().date()
    name = 'Dave'
    _context = {'date': date, 'name': name}
    return render(reguest, 'home.html', _context)