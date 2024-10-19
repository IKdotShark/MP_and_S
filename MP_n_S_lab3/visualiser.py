import matplotlib.pyplot as plt

# Визуализация частотного теста
class FrequencyTestVisualizer:
    def __init__(self, generator, built_in_generator):
        self.generator = generator
        self.built_in_generator = built_in_generator

    def visualize_frequency_test(self, num_samples):
        lcg_values = []
        random_values = []

        for _ in range(num_samples):
            # ЛКГ
            lcg_value = self.generator.next_double()
            lcg_values.append(lcg_value)

            # Встроенный генератор
            random_value = self.built_in_generator.next_double()
            random_values.append(random_value)

        # Построение гистограмм
        plt.figure(figsize=(10, 5))

        # Гистограмма для ЛКГ
        plt.subplot(1, 2, 1)
        plt.hist(lcg_values, bins=50, range=(0, 1), alpha=0.75, color='blue', label="LCG")
        plt.title("Частотный тест для ЛКГ")
        plt.xlabel("Значения")
        plt.ylabel("Частота")
        plt.grid(True)

        # Гистограмма для встроенного генератора
        plt.subplot(1, 2, 2)
        plt.hist(random_values, bins=50, range=(0, 1), alpha=0.75, color='green', label="Random")
        plt.title("Частотный тест для встроенного random")
        plt.xlabel("Значения")
        plt.ylabel("Частота")
        plt.grid(True)

        plt.tight_layout()
        plt.show()