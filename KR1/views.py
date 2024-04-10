from django.shortcuts import render
import sqlite3

def index(request):
    c = sqlite3.connect('Cargo.sqlite')
    car = c.cursor()
    car.execute("SELECT CargoName, CargoWeight, CargoVolume, Sender, Recipient, DataOfDispatch, Status FROM Cargo")
    test1 = car.fetchall()
    return render(request, 'index.html', {'test1': test1})

