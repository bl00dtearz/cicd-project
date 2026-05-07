from flask import Blueprint, request, jsonify
import logging


logging.basicConfig(
    filename='logs/app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

main = Blueprint('main', __name__)


@main.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'World')

    if len(name) > 50:
        logger.warning(f"Слишком длинное имя: {len(name)} символов")
        return jsonify({"error": "Имя слишком длинное"}), 400

    logger.info(f"Запрос приветствия для: {name}")
    return jsonify({"message": f"Hello, {name}!"})


@main.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()

    if not data or 'a' not in data or 'b' not in data:
        return jsonify({"error": "Нужны поля 'a' и 'b'"}), 400

    try:
        a = float(data['a'])
        b = float(data['b'])
    except (ValueError, TypeError):
        logger.warning("Неверный ввод в калькуляторе")
        return jsonify({"error": "Только числа!"}), 400

    result = a + b
    logger.info(f"Калькулятор: {a} + {b} = {result}")
    return jsonify({"result": result})


todos = []


@main.route('/todos', methods=['GET'])
def get_todos():
    logger.info("Получен список задач")
    return jsonify({"todos": todos})


@main.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()

    if not data or 'task' not in data:
        return jsonify({"error": "Нужно поле 'task'"}), 400

    task = str(data['task'])[:100]
    todos.append(task)
    logger.info(f"Добавлена задача: {task}")
    return jsonify({"message": "Задача добавлена", "task": task}), 201
