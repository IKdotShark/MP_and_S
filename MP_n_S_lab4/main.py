import time
from simulation import run_simulation


def main():
    num_counters = 10
    arrival_rate = 0.65
    sim_duration = 12 * 60
    tests = 3
    iterations = 1000

    start = time.time()
    report = run_simulation(num_counters, arrival_rate, sim_duration, tests, iterations)
    end_time = time.time()
    print(f"Симуляция завершена за {end_time - start:.3f} сек")
    report.display_params(num_counters, arrival_rate, sim_duration)
    report.summarize_results()
    report.save_log()
    report.draw_charts(arrival_rate)


if __name__ == "__main__":
    main()
