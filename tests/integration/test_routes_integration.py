import pytest
from flaskr import create_app

@pytest.fixture
def client():
    with create_app().test_client() as client:
        yield client

# Not sure if first two count as integration tests
def test_hello_route(client):
    rv = client.get('/hello')
    assert b'Hello, World!' in rv.data

def test_home_route(client):
    rv = client.get('/')
    assert b'Welcome to Battleship' in rv.data

    # Check for inputs
    assert b'<input name="X" placeholder="input X">\n            <input name="Y" placeholder="input Y">\n            <input type="submit" value="Submit">' in rv.data

# This is definitely an integration test
def test_calculate_post(client):
    rv = client.post('/calculate', data=dict(X=3,Y=0))
    print(rv.data)
    assert b'Welcome to Battleship' in rv.data

    # Check the first row to see if we calculated the board properly after request
    assert b'<td>X</td>\n                \n                <td>0</td>\n                \n                <td>0</td>\n                \n                <td>0</td>\n                \n                <td>0</td>\n' in rv.data