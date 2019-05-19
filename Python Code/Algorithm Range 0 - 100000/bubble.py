from random import *                     # Import python random module

def random_array(n):                     # Function takes as input a value n 
    array = []                           # create an array variable
    for i in range(0, n, 1):             # i start at 0 stop at n an increment by 1 (e.g. if n=4 0,1,2,3)
        array.append(randint(0,100))     # Add random generated integers with values between 0 and 99 to the array
    return array

# assign the random array to alist
alist1= random_array(100)
alist2= random_array(500)
alist3= random_array(1000)
alist4 = random_array(2500)
alist5 = random_array(5000)
alist6 = random_array(1000)
alist7 = random_array(20000)
alist8 = random_array(30000)
alist9 = random_array(40000)
alist10 = random_array(50000)
alist11 = random_array(60000)
alist12 = random_array(70000)
alist13 = random_array(80000)
alist14 = random_array(90000)
alist15 = random_array(100000)


# Code adapted from: https://www.geeksforgeeks.org/bubble-sort/
def bubbleSort(alist):              
    n = len(alist)
    for i in range(n):                                                   # Traverse through all elements in the array
        for j in range(0, n-i-1):                                        # Last i elements are already in place
            if alist[j] > alist[j+1]:                                    # Swap if the element is greater than the next element
                alist[j], alist[j+1] = alist[j+1], alist[j]

import time                                         # import time module

num_runs = 10                                       # Number of times to test the function i.e. we want 10 runs
results = []                                        # array to store results for each test
bubble_avglist = [] 

def benchmark_bubble():
    
    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        bubbleSort(alist1)                          # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    bubble_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        bubbleSort(alist2)                           # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    bubble_avglist.append(average)


    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        bubbleSort(alist3)                            # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    bubble_avglist.append(average)


    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        bubbleSort(alist4)                          # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    bubble_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        bubbleSort(alist5)                          # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    bubble_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        bubbleSort(alist6)                          # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    bubble_avglist.append(average)


    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        bubbleSort(alist7)                          # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    bubble_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        bubbleSort(alist8)                          # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    bubble_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        bubbleSort(alist9)                          # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    bubble_avglist.append(average)


    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        bubbleSort(alist10)                         # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    bubble_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        bubbleSort(alist11)                         # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    bubble_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        bubbleSort(alist12)                         # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    bubble_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        bubbleSort(alist13)                         # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    bubble_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        bubbleSort(alist14)                         # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    bubble_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        bubbleSort(alist15)                         # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    bubble_avglist.append(average)

    print(bubble_avglist)

benchmark_bubble()
