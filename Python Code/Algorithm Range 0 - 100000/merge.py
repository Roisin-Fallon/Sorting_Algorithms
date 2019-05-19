from random import *                     # Import python random module

def random_array(n):                     # Function takes as input a value n 
    array = []                           # create an array variable
    for i in range(0, n, 1):             # i start at 0 stop at n an increment by 1 (e.g. if n=4 0,1,2,3)
        array.append(randint(0,100))     # Add random generated integers with values between 0 and 99 to the array
    return array

# Assign random array to alist
alist1= random_array(100)
alist2= random_array(500)
alist3= random_array(1000)
alist4 = random_array(2500)
alist5 = random_array(5000)
alist6 = random_array(10000)
alist7 = random_array(20000)
alist8 = random_array(30000)
alist9 = random_array(40000)
alist10 = random_array(50000)
alist11 = random_array(60000)
alist12 = random_array(70000)
alist13 = random_array(80000)
alist14 = random_array(90000)
alist15 = random_array(100000)

# ref. Project.pdf
# importing the random numbers
from random import *

#Adapted from: https://www.geeksforgeeks.org/merge-sort/

def mergeSort(alist):

    #print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2                  # Find the middle of the array
       
        L = alist[:mid]                         # Divide the list elements into 2 halfs: right and left
        R = alist[mid:]

        mergeSort(L)                            # Sort the left half
        mergeSort(R)                            # Sort the right half

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                alist[k] = L[i]
                i+=1
            else:
                alist[k]=R[j]
                j+=1
            k+=1

        while i < len(L):                        # Check if an element is left 
            alist[k]=L[i]
            i+=1
            k+=1

        while j < len(R):                         # Check if element if right
            alist[k]=R[j]
            j+=1
            k+=1


import time                                         # import time module

num_runs = 10                                       # Number of times to test the function i.e. we want 10 runs
results = []                                        # array to store results for each test
merge_avglist = [] 

def benchmark_merge():
    
    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        mergeSort(alist1)                           # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    merge_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        mergeSort(alist2)                       # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    merge_avglist.append(average)


    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        mergeSort(alist3)                       # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    merge_avglist.append(average)


    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        mergeSort(alist4)                       # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    merge_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        mergeSort(alist5)                       # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    merge_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        mergeSort(alist6)                       # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    merge_avglist.append(average)


    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        mergeSort(alist7)                       # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    merge_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        mergeSort(alist8)                       # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    merge_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        mergeSort(alist9)                       # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    merge_avglist.append(average)


    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        mergeSort(alist10)                       # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    merge_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        mergeSort(alist11)                       # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    merge_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        mergeSort(alist12)                       # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    merge_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        mergeSort(alist13)                       # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    merge_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        mergeSort(alist14)                       # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    merge_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        mergeSort(alist15)                       # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    merge_avglist.append(average)
    
    print(merge_avglist)
    
benchmark_merge()


