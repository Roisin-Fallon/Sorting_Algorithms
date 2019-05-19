from random import *                     # Import python random module

def random_array(n):                     # Function takes as input a value n 
    array = []                           # create an array variable
    for i in range(0, n, 1):             # i start at 0 stop at n an increment by 1 (e.g. if n=4 0,1,2,3)
        array.append(randint(0,100))     # Add random generated integers with values between 0 and 99 to the array
    return array

# Assign random array to alist
alist1= random_array(100)
alist2= random_array(250)
alist3= random_array(500)
alist4 = random_array(750)
alist5 = random_array(1000)
alist6 = random_array(1250)
alist7 = random_array(2500)
alist8 = random_array(3750)
alist9 = random_array(5000)
alist10 = random_array(6250)
alist11 = random_array(7500)
alist12 = random_array(8750)
alist13 = random_array(10000)
alist14 = random_array(15000)
alist15 = random_array(20000)

# Adapted from: http://www.learntosolveit.com/python/algorithm_countingsort.html

def countingSort(array, maxval):
    """in-place counting sort"""
    n = len(array)
    m = maxval + 1
    count = [0] * m                                 # init with zeros
    for a in array:
        count[a] += 1                               # count occurences
    i = 0
    for a in range(m):                              # emit
        for c in range(count[a]):                   # - emit 'count[a]' copies of 'a'
            array[i] = a
            i += 1
    return (array,count)

import time                                         # import time module

num_runs = 10                                       # Number of times to test the function i.e. we want 10 runs
results = []                                        # array to store results for each test
countsort_avglist = [] 

def benchmark_countingsort():
    
    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        countingSort(alist1,100)                    # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    countsort_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        countingSort(alist2,250)                    # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    countsort_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        countingSort(alist4,500)                    # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    countsort_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        countingSort(alist4,750)                    # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    countsort_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        countingSort(alist5,1000)                   # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    countsort_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        countingSort(alist6,1250)                   # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    countsort_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        countingSort(alist7,2500)                   # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    countsort_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        countingSort(alist8,3750)                   # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    countsort_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        countingSort(alist9,5000)                   # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    countsort_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        countingSort(alist10,6250)                 # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    countsort_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        countingSort(alist11,7500)                  # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    countsort_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        countingSort(alist12,8750)                  # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    countsort_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        countingSort(alist13,10000)                 # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    countsort_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        countingSort(alist14,15000)                 # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    countsort_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        countingSort(alist15,20000)                 # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    countsort_avglist.append(average)
   
    print(countsort_avglist)

benchmark_countingsort()
