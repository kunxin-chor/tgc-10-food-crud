from flask import Flask, render_template, request, redirect, url_for
import os
import json
import random

app = Flask(__name__)
database = {}
with open('foods.json') as fp:
    database = json.load(fp)


@app.route('/foods')
def show_food():
    return render_template('foods.template.html', all_food=database)


@app.route('/foods/add')
def show_add_food():
    return render_template('add_food.template.html')


@app.route('/foods/add', methods=["POST"])
def process_add_food():
    new_food = {}
    new_food['food_name'] = request.form.get('food_name')
    new_food['when_eaten'] = request.form.get('when_eaten')
    new_food['meal'] = request.form.get('meal')
    new_food['calories'] = request.form.get('calories')
    new_food['id'] = random.randint(0, 100000)

    # add to the database
    database.append(new_food)

    # save back to the JSON file
    with open('foods.json', 'w') as fp:
        json.dump(database, fp)

    return redirect(url_for('show_food'))


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
