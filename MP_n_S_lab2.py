import random

# Определение состояний
STATES = ["Проверка карты", "Ответ банка", "Проверка наличия средств"]

# Определение входных сигналов
SIGNALS = {
    "Данные карты": 0,
    "Подтверждение банка": 1,
    "Отрицательный ответ банка": 2
}

# Таблица переходов (вероятности для каждого состояния)
TRANSITIONS = {
    "Проверка карты": {
        "Данные карты": [0.075, 0.9, 0.025],
        "Подтверждение банка": [0.9, 0.025, 0.075],
        "Отрицательный ответ банка": [0.9, 0.025, 0.075]
    },
    "Ответ банка": {
        "Данные карты": [0.075, 0.9, 0.025],
        "Подтверждение банка": [0.075, 0.025, 0.9],
        "Отрицательный ответ банка": [0.9, 0.025, 0.075]
    },
    "Проверка наличия средств": {
        "Данные карты": [0.075, 0.025, 0.9],
        "Подтверждение банка": [0.95, 0.025, 0.025],
        "Отрицательный ответ банка": [0.9, 0.025, 0.075]
    }
}


def choose_next_state(probabilities):
    """Функция для выбора следующего состояния на основе вероятностей"""
    return random.choices(STATES, probabilities)[0]


def main():
    current_state = "Проверка карты"
    print(f"Начальное состояние: {current_state}")

    while True:
        # Получаем входной сигнал от пользователя
        signal = input(f"Введите сигнал ({', '.join(SIGNALS.keys())}) или 'выход' для завершения: ")

        if signal == "выход":
            print("Завершение программы.")
            break

        if signal not in SIGNALS:
            print("Некорректный сигнал. Попробуйте снова.")
            continue

        # Выводим вероятности переходов для текущего состояния и выбранного сигнала
        probabilities = TRANSITIONS[current_state][signal]
        print(f"Вероятности переходов из состояния '{current_state}' по сигналу '{signal}':")
        for state, prob in zip(STATES, probabilities):
            print(f"  {state}: {prob}")

        # Выбираем следующее состояние на основе текущего состояния и входного сигнала
        next_state = choose_next_state(probabilities)
        print(f"Переход из '{current_state}' в '{next_state}' (сигнал: {signal})\n")

        current_state = next_state


if __name__ == "__main__":
    main()