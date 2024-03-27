from flask import Blueprint, render_template, request, jsonify
import requests

# Créer un blueprint
views_bp = Blueprint('views', __name__)

# Importer les vues depuis item_views.py
from . import views_bp

# Définir les routes et les vues
@views_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        api_url = f'https://api.beta.dofusdb.fr/items?name.fr={query}'
        response = requests.get(api_url)
        data = response.json()
        data_array = data.get('data', [])

        if data_array:
            print(data_array)
            return jsonify(data_array)
        else:
            return jsonify({'message': 'No data found for the provided query'})

    return render_template('index.html')

# Définir d'autres routes et vues au besoin
