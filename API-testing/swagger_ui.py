import requests

base_url = "https://fakerestapi.azurewebsites.net/"

def test_list_users():
    users_number:int = 0

    endpoint = "api/v1/Users"
    url = base_url+endpoint
    response = requests.get(url)
    
    for x in response.json():
        users_number+=1
    
    assert users_number == 10
    assert response.status_code == 200

def test_single_user_found():
    endpoint = "api/v1/Users/3"
    url = base_url+endpoint
    response = requests.get(url)

    assert response.json()['id'] == 3

def test_single_user_not_found():
    endpoint = "api/v1/Users/20"
    url = base_url+endpoint
    response = requests.get(url)

    assert response.status_code == 404
    assert response.reason == "Not Found"

def test_create_valid_user():
    endpoint = "api/v1/Users"
    url = base_url+endpoint

    request_data = {
        "id": 11,
        "userName": "User 11",
        "password": "Password11"
    }

    request_body = requests.post(url, json=request_data)

    assert request_body.request.method == "POST"

def test_create_invalid_user():
    endpoint = "api/v1/Users"
    url = base_url+endpoint

    request_data = {
        "id": 12,
        "username": 12,
        "password":  12
    }

    request_body = requests.post(url, json=request_data)

    assert request_body.status_code == 400
    assert request_body.reason == "Bad Request"