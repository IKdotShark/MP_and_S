# lcg_module.py

class LinearCongruentialGenerator:
    def __init__(self, a, c, m, seed):
        self.a = a  # Множитель
        self.c = c  # Приращение
        self.m = m  # Модуль
        self.current = seed  # Начальное значение

    def next_double(self):
        self.current = (self.a * self.current + self.c) % self.m
        return self.current / self.m  # Нормализуем в диапазон [0, 1]

    def next_long(self):
        self.current = (self.a * self.current + self.c) % self.m
        return self.current
