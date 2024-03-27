from flask import current_app, g
import os 
import sqlite3

def init_app(app):
    app.teardown_appcontext(close_db)
    # Check if the database is initialized
    if not os.path.exists(current_app.config['DATABASE']):
        with app.app_context():
            init_db()

def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES        
        )
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()