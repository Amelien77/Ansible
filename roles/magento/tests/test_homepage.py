#Vérifie si la page d'accueil de Magento est accessible

import requests

def test_homepage():
    response = requests.get('http://10.0.136.194/')
    assert response.status_code == 200
