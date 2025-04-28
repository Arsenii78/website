from requests import get, post

print(get('http://127.0.0.1:5000/api/user').json())

print(get('http://127.0.0.1:5000/api/user/1').json())

print(get('http://127.0.0.1:5000/api/user/999').json())
