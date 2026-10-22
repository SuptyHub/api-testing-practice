import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_single_post():
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "title" in data


def test_get_all_posts():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    data = response.json()
    assert len(response.json()) > 0


def test_get_posts():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200

    posts = response.json()
    assert len(posts) == 100
    assert "title" in posts[0]


def test_get_XNotFound():
    response = requests.get(f"{BASE_URL}/posts/99999")
    assert response.status_code == 404


def test_this_must_fail():
    assert 1 == 2
