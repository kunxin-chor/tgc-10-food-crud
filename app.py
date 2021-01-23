from flask import Flask, render_template, request, redirect, url_for
import os
import json

app = Flask(__name__)
database = {}
with open('foods.json') as fp:
    database = json.load(fp)


@app.route('/foods')
def show_food():
    return render_template('foods.template.html', all_food=database)


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
