# Author: Norvin Lim
# Date: 2024-02-06
# Executed already

import random
import time
import statistics

def fut(case):
    fut2(case, 0, len(case) - 1)
    return case


def fut2(case, s, t):
    if t < s:
        return
    if case[s] > case[t]:
        case[s], case[t] = case[t], case[s]
    if t > s + 1:
        q = (t - s + 1) // 3
        fut2(case, s, t - q)
        fut2(case, s + q, t)
        fut2(case, s, t - q)

def fut_measure(input):
    """
    Measures Average time in nanoseconds of the fut function.
    This function is copy pasted from Routines 1 through 5
    Args:
        input (list): Input data is passed to the fut function

    Returns:
        int: Average execution time represented in Nanoseconds
    """
    time0 = time.perf_counter_ns()  # Record starting time
    fut(input)  # Execute the function to measure
    time1 = time.perf_counter_ns()  # Record ending time
    return time1 - time0  # Calculate and return the elapsed time in nanoseconds

def casemaker(size):
    return [random.randint(0, 10**9) for _ in range(size)]

# Testing List sizes/case numbers.
# All commented out lists are those unused.
# list_sizes_0 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
# list_sizes_1 = [3, 6, 9, 12, 24, 48,  96, 192, 384, 768]
# list_sizes_2 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
# list_sizes_3 = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
# list_sizes_4 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
list_sizes_5 = [200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000]
# list_sizes_6 = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
# list_sizes_7 = [10**4, 20**4, 30**4, 40**4, 50**4, 60**4, 70**4, 80**4, 90**4, 100**4]

# Empty list to store results of chosen execution
list_of_results = []

# This bottom section is the same for all routines. It's just the upper segments for function tests are different. Only differences would be the sample/test size/number
for size in list_sizes_5:
    executed_time = [] # List to store execution time of executed algo
    times_to_run = 20 # Number of times to execute the algo
    test_case = casemaker(size)

    for _ in range(times_to_run):
        time_execution = fut_measure(test_case)
        executed_time.append(time_execution)
    mean_execution_time = statistics.mean(executed_time)
    list_of_results.append((size, mean_execution_time, times_to_run ))

for size, mean_execution_time, time_execution in list_of_results:
    print(f"Sample/Test Size: {size} --- Mean Runtime = {mean_execution_time} --- Times Executed {time_execution}")
    