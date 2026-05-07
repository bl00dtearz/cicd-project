import pytest
from app import create_app


@pytest.fixture
def client():
    """Создаём тестовый клиент — имитирует браузер/запросы"""
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


# --- Тесты Фичи 1: Приветствие ---
def test_greet_default(client):
    """Без имени должно вернуть Hello, World!"""
    response = client.get('/greet')
    assert response.status_code == 200
    assert b'Hello, World!' in response.data


def test_greet_with_name(client):
    """С именем должно вернуть Hello, Amir!"""
    response = client.get('/greet?name=Amir')
    assert response.status_code == 200
    assert b'Amir' in response.data


def test_greet_too_long_name(client):
    """Слишком длинное имя должно вернуть ошибку 400"""
    long_name = 'A' * 100
    response = client.get(f'/greet?name={long_name}')
    assert response.status_code == 400


# --- Тесты Фичи 2: Калькулятор ---
def test_calculate_sum(client):
    """2 + 3 должно вернуть 5"""
    response = client.post('/calculate', json={'a': 2, 'b': 3})
    assert response.status_code == 200
    assert response.get_json()['result'] == 5.0


def test_calculate_invalid_input(client):
    """Текст вместо чисел — ошибка 400"""
    response = client.post('/calculate', json={'a': 'abc', 'b': 3})
    assert response.status_code == 400


def test_calculate_missing_fields(client):
    """Пустой запрос — ошибка 400"""
    response = client.post('/calculate', json={})
    assert response.status_code == 400


# --- Тесты Фичи 3: Todo ---
def test_get_todos(client):
    """Получить список задач — статус 200"""
    response = client.get('/todos')
    assert response.status_code == 200


def test_add_todo(client):
    """Добавить задачу — статус 201"""
    response = client.post('/todos', json={'task': 'Сделать задание'})
    assert response.status_code == 201
    assert b'task' in response.data


def test_add_todo_missing_field(client):
    """Запрос без поля task — ошибка 400"""
    response = client.post('/todos', json={})
    assert response.status_code == 400