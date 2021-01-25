from flask import Flask, render_template, request, redirect, url_for
import os
import json
import random

app = Flask(__name__)
database = {}
with open('foods.json') as fp:
    database = json.load(fp)


def find_food_by_id(food_id):
    wanted_food_record = None
    for food_record in database:
        if food_record["id"] == food_id:
            wanted_food_record = food_record
            # stop the for loop since we already found
            # what we want
            break

    return wanted_food_record


@app.route('/')
def index():
    return "Welcome"


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


@app.route('/foods/<int:food_id>/update')
def show_update_food(food_id):
    # linear search to find the record that we want to edit
    wanted_food_record =find_food_by_id(food_id)

    return render_template('update_food.template.html',
                           food=wanted_food_record)


@app.route('/foods/<int:food_id>/update', methods=["POST"])
def process_update_food(food_id):
    # do a linear search to find the food we are updating
    existing_food_record = find_food_by_id(food_id)
    existing_food_record['food_name'] = request.form.get('food_name')
    existing_food_record['when_eaten'] = request.form.get('when_eaten')
    existing_food_record['meal'] = request.form.get('meal')
    existing_food_record['calories'] = request.form.get('calories')

    return redirect(url_for('show_food'))


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
