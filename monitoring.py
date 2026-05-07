"""
Part 7: Скрипт мониторинга — читает логи и показывает статистику
"""
import os
from collections import Counter


def analyze_logs(log_file: str = 'logs/app.log') -> None:
    """Анализирует лог-файл и выводит статистику"""

    if not os.path.exists(log_file):
        print("Лог-файл не найден. Запусти приложение сначала.")
        return

    levels = []
    lines = []

    with open(log_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for line in lines:
        if '- INFO -' in line:
            levels.append('INFO')
        elif '- WARNING -' in line:
            levels.append('WARNING')
        elif '- ERROR -' in line:
            levels.append('ERROR')
        elif '- DEBUG -' in line:
            levels.append('DEBUG')

    stats = Counter(levels)

    print("=" * 40)
    print("МОНИТОРИНГ ЛОГОВ ПРИЛОЖЕНИЯ")
    print("=" * 40)
    print(f"Всего записей : {len(lines)}")
    print(f"INFO          : {stats.get('INFO', 0)}")
    print(f"WARNING       : {stats.get('WARNING', 0)}")
    print(f"ERROR         : {stats.get('ERROR', 0)}")
    print(f"DEBUG         : {stats.get('DEBUG', 0)}")
    print("=" * 40)

    if stats.get('ERROR', 0) > 0:
        print("Обнаружены ошибки! Проверь логи.")
    elif stats.get('WARNING', 0) > 0:
        print("Есть предупреждения. Всё под контролем.")
    else:
        print("Всё работает нормально!")


if __name__ == '__main__':
    analyze_logs()
