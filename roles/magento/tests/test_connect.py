import requests

def test_magento_homepage():
    url = 'http://10.0.136.194' 
    response = requests.get(url)
    assert response.status_code == 200
