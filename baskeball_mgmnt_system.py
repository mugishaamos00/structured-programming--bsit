from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('db.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/teams', methods=['GET', 'POST'])
def teams():
    conn = get_db_connection()
    if request.method == 'POST':
        data = request.json
        conn.execute('INSERT INTO teams (name, coach) VALUES (?, ?)', 
                     (data['name'], data['coach']))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Team added!'}), 201
    else:
        teams = conn.execute('SELECT * FROM teams').fetchall()
        conn.close()
        return jsonify([dict(row) for row in teams])

@app.route('/players', methods=['GET', 'POST'])
def players():
    conn = get_db_connection()
    if request.method == 'POST':
        data = request.json
        conn.execute('INSERT INTO players (name, team_id, position) VALUES (?, ?, ?)', 
                     (data['name'], data['team_id'], data['position']))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Player added!'}), 201
    else:
        players = conn.execute('SELECT * FROM players').fetchall()
        conn.close()
        return jsonify([dict(row) for row in players])

@app.route('/matches', methods=['GET', 'POST'])
def matches():
    conn = get_db_connection()
    if request.method == 'POST':
        data = request.json
        conn.execute('INSERT INTO matches (team1_id, team2_id, score1, score2, date) VALUES (?, ?, ?, ?, ?)', 
                     (data['team1_id'], data['team2_id'], data['score1'], data['score2'], data['date']))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Match added!'}), 201
    else:
        matches = conn.execute('SELECT * FROM matches').fetchall()
        conn.close()
        return jsonify([dict(row) for row in matches])

if __name__ == '__main__':
    app.run(debug=True)