# Prevent RecursionError: maximum recursion depth exceeded in comparison
import sys
sys.setrecursionlimit(1500)             # Default is 1000 so I increased it to 1000

from random import *                     # Import random number

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

# Adapted from: https://www.pythoncentral.io/quick-sort-implementation-guide/

def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)                # recursive function 

# Sorts the list from indexes first to last 
def quickSortHelper(alist,first,last):                  
   if first<last:                                           

       splitpoint = partition(alist,first,last)       # we call a partition functtion which does most of the work of the quicksort and returns the pivot around which we partition the list 

       quickSortHelper(alist,first,splitpoint-1)      # for all items left of the pivot we will call quicksortHelrper again recursively 
       quickSortHelper(alist,splitpoint+1,last)        # r all items right of the pivot we will call quicksortHelper again recursively 

def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp

   return rightmark

import time                                         # import time module

num_runs = 10                                       # Number of times to test the function i.e. we want 10 runs
results = []                                        # Array to store results for each test
quicksort_avglist = [] 

def benchmark_quick():
    
    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        quickSort(alist1)                           # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    quicksort_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        quickSort(alist2)                           # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    quicksort_avglist.append(average)


    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        quickSort(alist3)                           # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    quicksort_avglist.append(average)


    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        quickSort(alist4)                           # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    quicksort_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        quickSort(alist5)                           # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    quicksort_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        quickSort(alist6)                           # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    quicksort_avglist.append(average)


    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        quickSort(alist7)                           # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    quicksort_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        quickSort(alist8)                           # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    quicksort_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        quickSort(alist9)                           # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    quicksort_avglist.append(average)


    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        quickSort(alist10)                          # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    quicksort_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        quickSort(alist11)                          # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    quicksort_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        quickSort(alist12)                          # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    quicksort_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        quickSort(alist13)                          # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    quicksort_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        quickSort(alist14)                          # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    quicksort_avglist.append(average)

    for r in range(num_runs):                       # Benchmark the function
        start_time = time.time()                    # Log the start time in seconds
        quickSort(alist15)                          # Call the function insertion to benchmark
        end_time = time.time()                      # Log the end time in seconds
        time_elapsed= end_time - start_time         # Calculate the elapsed time 
        results.append(time_elapsed)

    b = sum(results)                                # Sum the results of the 10 runs
    average = (b/num_runs)                          # Calculate the average of a run
    quicksort_avglist.append(average)

    print(quicksort_avglist)

benchmark_quick()

