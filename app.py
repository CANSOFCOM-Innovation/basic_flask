import csv
import sys

from flask import Flask, render_template

reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__)


@app.route('/')
def index():
    restaurants = open_file()
    return render_template('index.html', restaurants=restaurants)


def open_file():
    with open('tripadvisor_in-restaurant_sample.csv', 'rb') as infile:
        data = [row for row in csv.DictReader(infile)]
    return data


if __name__ == '__main__':
    app.run(debug=True)

