from flask import Flask, render_template, request, jsonify
from random import shuffle

app = Flask(__name__)
# for config (if needed)
app.config.from_object(__name__)


@app.route('/')
def index():
    return render_template('form.html')


@app.route('/generate', methods=['POST'])
def create_teams():
    animals = ['Hawks', 'Cobras', 'Squirrels', 'Giraffes', 'Sheep', 'Dogs', 'Rats', 'Pigs', 'Ducks', 'Cheetahs']
    colours = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet', 'Magento', 'Black', 'White', 'Beige']
    numbers = ['Team 1', 'Team 2', 'Team 3', 'Team 4', 'Team 5', 'Team 6', 'Team 7', 'Team 8', 'Team 9', 'Team 10']

    num_teams = int(request.form['number_teams'])
    names = request.form['names'].split('\r\n')
    team_names = request.form['team_names']
    teams = {}

    shuffle(names)

    if(team_names == 'numbers'):
        for i in range(num_teams):
            teams[numbers[i]] = []

    elif(team_names == 'animals'):
        for i in range(num_teams):
            teams[animals[i]] = []

    elif(team_names == 'colours'):
        for i in range(num_teams):
            teams[colours[i]] = []

    # while names
    while len(names) > 0:
        # loop through teams
        for team in teams:
            # pop name from names and add to team
            if len(names) > 0:
                teams[team].append(names.pop().strip())

    sorted(teams)

    return jsonify(teams)


if __name__ == '__main__':
    app.run()
