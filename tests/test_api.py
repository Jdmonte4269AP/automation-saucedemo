# x-api-key: pub_5bca5ffc8772df976fcf8970168a1ad219ad499c472afbba2f27085fa4b4ef7d

import requests

def test_obtener_usuario(base_url,headers):
    url = f"{base_url}/users/2"

    response = requests.get(url,headers=headers)

    # NIVEL 1: STATUS CODE
    codigo = response.status_code
    assert codigo == 200

    # NIVEL 2: HEADERS
    assert "application/json" in response.headers["Content-Type"]

    # NIVEL 3: ESTRUCTURA
    data = response.json()

    assert isinstance(data,dict) # Validar que el contenido sea un diccionario
    assert "data" in data
    assert isinstance(data["data"],dict)

    assert "id" in data["data"]
    assert "email" in data["data"]
    assert "first_name" in data["data"]
    assert "last_name" in data["data"]

    # NIVEL 4: CONTENIDO
    assert data["data"]["id"] == 2
    assert data["data"]["email"] == "janet.weaver@reqres.in"

    # NIVEL 5: TIEMPO DE RESPUESTA
    assert response.elapsed.total_seconds() < 2


def test_crear_usuario(base_url,headers):
    url = f"{base_url}/users/"

    usuario = {
        "email":"jose.montezuma@bue.edu.ar",
        "first_name":"Jose",
        "last_name":"Montezuma",
        "job":"Instructor"
    }

    response = requests.post(url,headers=headers,json=usuario)

    # NIVEL 1
    assert response.status_code == 201

    # NIVEL 2
    assert "application/json" in response.headers["Content-Type"]

    # NIVEL 3
    data = response.json()
    assert "email" in data
    assert "first_name" in data
    assert "last_name" in data
    assert "id" in data

    # NIVEL 4
    assert data["email"] == usuario["email"]
    assert data["first_name"] == usuario["first_name"]

    # NIVEL 5: TIEMPO DE RESPUESTA
    assert response.elapsed.total_seconds() < 2

def test_eliminar_usuario(base_url,headers):
    url = f"{base_url}/users/2"
    
    response = requests.delete(url,headers=headers)
    
    # NIVEL 1: STATUS CODE
    assert response.status_code == 204
    
    # NIVEL 2: HEADERS
    assert "Content-Type" not in response.headers
    
    # NIVEL 3 Y 4: ESTRUCTURA Y CONTENIDO
    assert len(response.content) == 0
    
    # NIVEL 5: TIEMPO DE RESPUESTA
    assert response.elapsed.total_seconds() < 2
    
"""
{
    "data":{
        "id":2,
        "email":"jose.montezuma@bue.edu.ar",
        "nombre":"Jose",
        "apellido":"Montezuma"
    },
    "support":{}
}
"""