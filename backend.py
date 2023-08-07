from config import app
from flask import request, render_template, redirect
from src.webScreenshot import getScreenshot
from src.pasportData import getRandomPasportData, getRandomPasportTransform
import os
from app import getPasportLinesData


@app.route('/', methods=['POST', 'GET'])
def main():
    pasportData: dict = getRandomPasportData()
    transform: list = getRandomPasportTransform()
    if request.method == 'POST':
        getScreenshot()
    return render_template('index.html', data=pasportData, transform=transform)


@app.route('/show/', methods=['POST', 'GET'])
def showsettings():
    dataList = []
    for root, dirs, files in os.walk("./screenshots"):
        for filename in files:
            dataList.append(filename.replace('.jpg', ''))

    if request.method == 'POST':
        pasportID = request.form['pasportid']
        return redirect(f'/show/{pasportID}')
    return render_template('showsettings.html', data=dataList)


@app.route('/show/<pasportid>')
def showpasport(pasportid):
    linesData = getPasportLinesData(pasportName=pasportid)
    return render_template('show.html', lines=linesData, pasportid=pasportid)


if __name__ == '__main__':
    app.run()
