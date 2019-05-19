
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

# Code adapted from: https://www.geeksforgeeks.org/python-program-for-insertion-sort/

def insertionSort(alist):                                   # Function to do insertion sort
     for i in range(1,len(alist)):                          # Start for loop at second element (index 1), assume the first element is sorted
        key=alist[i]                                        # Next element inserted into sorted section of array
        position = i -1                                     # Last element we are going to compare with

# Comparing the current element with the sorted position and swapping 
        while position>=0 and key < alist[position]:        # Move the key as long as it is less than the previous item in the array
            alist[position +1]=alist[position]              # Move the last element compared on step above to make room for key
            position -= 1                                   # The next item to compare
        alist[position+1]=key                               

import time                                         # import time module

num_runs = 10                                       # Number of times to test the function i.e. we want 10 runs
results = []                                        # array to store results for each test
insertsort_avglist = [] 

def benchmark_insertionsort():
    
    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        insertionSort(alist1)                       # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    insertsort_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        insertionSort(alist2)                       # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    insertsort_avglist.append(average)


    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        insertionSort(alist3)                       # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    insertsort_avglist.append(average)


    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        insertionSort(alist4)                       # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    insertsort_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        insertionSort(alist5)                       # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    insertsort_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        insertionSort(alist6)                       # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    insertsort_avglist.append(average)


    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        insertionSort(alist7)                       # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    insertsort_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        insertionSort(alist8)                       # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    insertsort_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        insertionSort(alist9)                       # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    insertsort_avglist.append(average)


    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        insertionSort(alist10)                       # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    insertsort_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        insertionSort(alist11)                       # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    insertsort_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        insertionSort(alist12)                       # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    insertsort_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        insertionSort(alist13)                       # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    insertsort_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        insertionSort(alist14)                       # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    insertsort_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        insertionSort(alist15)                       # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    insertsort_avglist.append(average)
  
    print(insertsort_avglist)

benchmark_insertionsort()
