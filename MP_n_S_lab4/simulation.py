from datetime import timedelta, datetime
import random
import numpy as np
from simulation_report import SimulationReport
from mat_utils import generate_exponential


def run_simulation(num_counters, arrival_rate, sim_duration, tests, iterations):
    results_report = SimulationReport()
    for test_num in range(tests):
        day_results = np.zeros(num_counters + 1)
        cashier_speeds = [round(random.uniform(0.5, 1.2), 2) for _ in range(num_counters)]
        cashier_speeds.sort()
        results_report.add_results(
            simulate_day(iterations, day_results, num_counters, arrival_rate, sim_duration, results_report,
                         cashier_speeds),
            cashier_speeds
        )
    return results_report


def simulate_day(iterations, day_results, num_counters, arrival_rate, sim_duration, results_report, cashier_speeds):
    inv_a = -1 / arrival_rate
    start_time = datetime.strptime("09:00:00", "%H:%M:%S")

    for _ in range(iterations):
        queue_times = np.zeros(num_counters)
        daily_time = 0

        while daily_time < sim_duration:
            next_arrival = generate_exponential(inv_a)
            client_items = random.randint(1, 30)
            daily_time += next_arrival

            process_customer(next_arrival, queue_times, day_results, num_counters, cashier_speeds,
                             client_items, start_time + timedelta(seconds=daily_time * 60), results_report)

    return day_results / iterations


def process_customer(next_arrival, queue_times, day_results, num_counters, cashier_speeds,
                     client_items, event_time, results_report):
    for idx in range(num_counters):
        if queue_times[idx] < next_arrival:
            cashier_speed = cashier_speeds[idx]
            service_time = client_items * cashier_speed
            day_results[idx] += 1
            queue_times[idx] = service_time
            results_report.log_event(event_time, idx + 1, cashier_speed, idx + 1, client_items)
            break
        if idx == num_counters - 1:
            day_results[-1] += 1

    queue_times[:] = [max(0, q - next_arrival) for q in queue_times]
