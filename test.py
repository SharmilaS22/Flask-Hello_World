from requests import get

def test_root():

    expected = {
        'msg' : 'Hello, world!'
    }
    response = get('http://localhost:5000/')
    assert response.json() == expected
    
    return 

if __name__ == '__main__':
    test_root()