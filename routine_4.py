# Author: Norvin Lim
# Date: 2024-02-06
# Executed Already

import random
import time
import statistics


def fut(case):
    result = 0
    trials = ["1"]
    while True:
        result += 1
        if "".join(trials) == case:
            return result
        i = len(trials) - 1
        while trials[i] == "1":
            trials[i] = "0"
            i -= 1
        if i == -1:
            trials = ["1"] + trials
        else:
            trials[i] = "1"
        if result > 1e24:
            return "WAT"


def casemaker(size):
    return "1" + "".join(random.choices("10", k=size))



def fut_measure(input):
    """
    Measures Average time in nanoseconds of the fut function

    Args:
        input (list): Input data is passed to the fut function

    Returns:
        int: Average execution time represented in Nanoseconds
    """
    time0 = time.perf_counter_ns()  # Record starting time
    fut(input)  # Execute the function to measure
    time1 = time.perf_counter_ns()  # Record ending time
    return time1 - time0  # Calculate and return the elapsed time in nanoseconds

# Testing List sizes/case numbers.
# All commented out lists are those unused.
# list_sizes_0 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
# list_sizes_1 = [3, 6, 9, 12, 24, 48,  96, 192, 384, 768]
# list_sizes_2 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
# list_sizes_3 = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70] This was the original selection however after +16hr of running no results came through
# list_sizes_4 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# list_sizes_5 = [200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000]
# list_sizes_6 = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
# list_sizes_7 = [10**4, 20**4, 30**4, 40**4, 50**4, 60**4, 70**4, 80**4, 90**4, 100**4]
list_sizes_8 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]  
# New set of numbers for case 

# Empty list to store results of chosen execution
list_of_results = []

for size in list_sizes_8:
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
    