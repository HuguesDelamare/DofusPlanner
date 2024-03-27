# Dans votre fichier views/item_views.py

from flask import Blueprint, render_template, request, jsonify
import requests

# Créer un blueprint pour les vues des items
item_views_bp = Blueprint('item_views', __name__)

# Définir la route pour la recherche d'objet
@item_views_bp.route('/search', methods=['POST'])
def search():
    query = request.form.get('query', '')  # Obtenir le terme de recherche depuis le formulaire
    api_url = f'https://api.beta.dofusdb.fr/items?name.fr={query}'
    response = requests.get(api_url)
    data = response.json()

    data_array = data.get('data', [])

    # Traiter les données, extraire les informations nécessaires, etc.
    extracted_data = []
    for item in data_array:
        extracted_item = {
            'id': item.get('_id'),
            'name': item.get('name', {}).get('fr'),
            'description': item.get('description', {}).get('fr'),
            'image': item.get('img'),
            'type': item.get('type', {}).get('name', {}).get('fr'),
            'level': item.get('level'),
            'stats': item.get('effects', [])
        }
        extracted_data.append(extracted_item)

    if extracted_data:
        # Retourner les données extraites au format JSON
        return jsonify(extracted_data)
    else:
        # Retourner un message indiquant qu'aucune donnée n'a été trouvée
        return jsonify({'message': 'No data found for the provided query'})
