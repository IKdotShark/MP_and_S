import math
from lcg_module import LinearCongruentialGenerator
from random_module import BuiltInRandomGenerator
from visualiser import FrequencyTestVisualizer

# Анализ псевдослучайных чисел
class RandomAnalyzer:
    def __init__(self, generator, built_in_generator):
        self.generator = generator
        self.built_in_generator = built_in_generator

    def analyze_random_numbers(self, num_samples):
        lcg_sum = 0
        random_sum = 0
        lcg_squared_sum = 0
        random_squared_sum = 0
        lcg_less_than_half = 0
        random_less_than_half = 0

        for _ in range(num_samples):
            # ЛКГ
            lcg_value = self.generator.next_double()
            lcg_sum += lcg_value
            lcg_squared_sum += lcg_value ** 2
            if lcg_value < 0.5:
                lcg_less_than_half += 1

            # Встроенный генератор
            random_value = self.built_in_generator.next_double()
            random_sum += random_value
            random_squared_sum += random_value ** 2
            if random_value < 0.5:
                random_less_than_half += 1

        # Математическое ожидание и дисперсия для ЛКГ
        lcg_mean = lcg_sum / num_samples
        lcg_variance = (lcg_squared_sum / num_samples) - (lcg_mean ** 2)
        lcg_standard_deviation = math.sqrt(lcg_variance)

        # Математическое ожидание и дисперсия для встроенного генератора
        random_mean = random_sum / num_samples
        random_variance = (random_squared_sum / num_samples) - (random_mean ** 2)
        random_standard_deviation = math.sqrt(random_variance)

        # Результаты
        print(f"ЛКГ: Математическое ожидание = {lcg_mean}, Дисперсия = {lcg_variance}, Среднеквадратичное отклонение = {lcg_standard_deviation}")
        print(f"Random: Математическое ожидание = {random_mean}, Дисперсия = {random_variance}, Среднеквадратичное отклонение = {random_standard_deviation}")

        # Сравнение попадания в интервалы
        print(f"ЛКГ: Процент значений < 0.5 = {(lcg_less_than_half / num_samples) * 100}%")
        print(f"Random: Процент значений < 0.5 = {(random_less_than_half / num_samples) * 100}%")


# Определение длины периода генератора
class PeriodAnalyzer:
    def __init__(self, generator):
        self.generator = generator

    def determine_period(self, max_iterations=1000000):
        seen_values = set()
        period = 0

        # Генерация чисел до первого повторения или достижения лимита
        while period < max_iterations:
            current = self.generator.next_long()

            if current in seen_values:
                print(f"Повторение найдено на итерации {period}")
                return period
            else:
                seen_values.add(current)
                period += 1

            if period % 100000 == 0:
                print(f"Прошло {period} итераций...")

        print("Повторение не найдено за максимально допустимое количество итераций.")
        return period



# Основная программа
def main():
    # Параметры ЛКГ
    a = 1673625  # Множитель
    c = 1013910000  # Приращение c = 1013910000
    m = 2 ** 34 # Рекомендуемое >= 2 ** 32
    seed = 12345  # Начальное значение

    lcg = LinearCongruentialGenerator(a, c, m, seed)
    built_in_random = BuiltInRandomGenerator()

    print("Выберите режим:")
    print("1. Генерация и анализ псевдослучайных чисел (с ЛКГ и random).")
    print("2. Определение длины периода генератора (ЛКГ).")
    print("3. Сравнение визуализаций частотного теста.")

    choice = int(input())

    if choice == 1:
        random_analyzer = RandomAnalyzer(lcg, built_in_random)
        random_analyzer.analyze_random_numbers(1000000)
    elif choice == 2:
        period_analyzer = PeriodAnalyzer(lcg)
        period = period_analyzer.determine_period(1000000)  # Максимум 1 миллион итераций
        print(f"Длина периода генератора: {period}")
        # for tests
        # математическое ожидание должно быть ~0.5
        # дисперсия ~ 0.0833
        # среднеквадратическое отклонение ~0,2887
    elif choice == 3:
        visualizer = FrequencyTestVisualizer(lcg, built_in_random)
        visualizer.visualize_frequency_test(100000)  # Число выборок для визуализации
    else:
        print("Некорректный выбор.")


if __name__ == "__main__":
    main()
