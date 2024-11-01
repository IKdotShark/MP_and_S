import numpy as np
import matplotlib.pyplot as plt


class SimulationReport:
    def __init__(self):
        self.data_storage = []
        self.test_count = 0
        self.log = []
        self.cashier_speeds = []

    def add_results(self, results_array, cashier_speeds):
        self.test_count += 1
        self.data_storage.append(results_array)
        self.cashier_speeds = cashier_speeds
        self._display_results_summary(results_array)

    def _display_results_summary(self, results_array):
        self._print_test_title()
        *counters, missed_clients = results_array
        for idx, count in enumerate(counters, 1):
            cashier_speed = self.cashier_speeds[idx - 1]
            print(f"Касса {idx}: {count:.3f} посетителей. (Скорость кассы: {cashier_speed:.2f} сек/товар)")
        print(f"Упущено клиентов: {missed_clients:.3f}\n")

    def display_params(self, num_counters, arrival_rate, simulation_duration):
        print(
            f"Количество касс: {num_counters}, Параметр a: {arrival_rate}, Время моделирования: {simulation_duration} мин")

    def summarize_results(self):
        aggregated_data = np.array(self.data_storage).T
        min_vals, mean_vals, max_vals = self._calc_stats(aggregated_data)

        for idx in range(len(mean_vals) - 1):
            self._print_stats(idx, min_vals, mean_vals, max_vals)
        self._print_stats(-1, min_vals, mean_vals, max_vals, is_missed=True)

    def draw_charts(self, rate_param):
        self._plot_func_chart(rate_param)
        self._plot_bars_chart()

    def _calc_stats(self, data_matrix):
        return np.min(data_matrix, axis=1), np.mean(data_matrix, axis=1), np.max(data_matrix, axis=1)

    def _plot_func_chart(self, rate_param):
        x_vals = np.linspace(0, 10, 400)
        y_vals = rate_param * np.exp(-rate_param * x_vals)

        plt.figure(figsize=(8, 6))
        plt.plot(x_vals, y_vals, label="f(x) = 1/a * exp(-ax)", color="blue")
        plt.title("График функции f(x) = 1/a * exp(-ax)")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.legend()
        plt.grid(True)
        plt.show(block=False)

    def _plot_bars_chart(self):
        mean_vals = np.mean(self.data_storage, axis=0)
        max_vals = np.max(self.data_storage, axis=0)
        diff_vals = max_vals - mean_vals
        positions = np.arange(len(mean_vals))

        plt.figure(figsize=(8, 6))
        plt.bar(positions, mean_vals, width=0.4, color="blue", label="Среднее")
        plt.bar(positions, diff_vals, width=0.4, bottom=mean_vals, color="orange", label="Максимальное")
        plt.xticks(positions, [f"Касса {i + 1}" for i in range(len(mean_vals) - 1)] + ["Упущено"])
        plt.title("Сравнение средних и максимальных значений")
        plt.xlabel("Категория")
        plt.ylabel("Значение")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def _print_test_title(self):
        print(f"Результаты теста №{self.test_count}")

    def _print_stats(self, idx, min_vals, mean_vals, max_vals, is_missed=False):
        label = "Упущено клиентов" if is_missed else f"Касса {idx + 1}"
        print(f"{label}: Минимальное = {min_vals[idx]}, Среднее = {mean_vals[idx]:.3f}, Максимальное = {max_vals[idx]}")

    def log_event(self, event_time, cashier_id, cashier_speed, counter_num, client_items):
        self.log.append(
            f"{event_time.strftime('%H:%M:%S')}: кассир-{cashier_id} ({cashier_speed:.2f} сек/товар), касса {counter_num}, клиент {client_items} товаров")

    def save_log(self, filename="simulation_log.txt"):
        with open(filename, "w", encoding="utf-8") as file:
            for entry in self.log:
                file.write(entry + "\n")
        print(f"Лог сохранён в {filename}")
