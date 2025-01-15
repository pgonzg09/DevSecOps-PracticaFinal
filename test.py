from app import app


def test_home_page():
    """Prueba la ruta principal"""
    response = app.test_client().get('/')
    print(response)
    assert response.status_code == 200
    assert b"Hello, CI/CD with Docker!" in response.data


def test_add():
    """Prueba la función de suma"""
    response = app.test_client().get('/add/2/3')
    assert response.status_code == 200
    assert b"2 + 3 = 5" in response.data


def test_sub():
    """Prueba la función de resta"""
    response = app.test_client().get('/sub/5/3')
    assert response.status_code == 200
    assert b"5 - 3 = 2" in response.data


def test_mult():
    """Prueba la función de multiplicación"""
    response = app.test_client().get('/mult/4/3')
    assert response.status_code == 200
    assert b"4 * 3 = 12" in response.data

    response = app.test_client().get('/mult/4/0')
    assert response.status_code == 200
    assert b"4 * 0 = 0" in response.data


def test_div():
    """Prueba la función de división"""
    response = app.test_client().get('/div/6/2')
    assert response.status_code == 200
    assert b"6 / 2 = 3.0" in response.data

    response = app.test_client().get('/div/6/0')
    assert response.status_code == 200
    assert b"Error: Division by 0 not allowed" in response.data


def test_invalid_routes():
    """Prueba rutas inválidas"""
    response = app.test_client().get('/invalid_route')
    assert response.status_code == 404
