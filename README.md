# Programming_and_Scripting_Project_2019


### Table of Contents

1. [ Introduction ](#intro)
    * [Concept of Sorting](#c)
    * [Relevance of sorting algorithm to the modern world](#r)
    * [ Sorting Algorithm Timeline](#his)
    * [Space Complexity](#sp)
    * [Time Complexity](#time)
2. [Simple Comparative Sorting Algorithms](#par)
    * [Bubble Sort](#bub)
    * [Insertion Sort](#in)
3. [Efficient Comparative Sorting Algorithms]
    * [Quick Sort](#quick)
    * [Merge Sort](#merge)
4. [Non-comparative Sorting Algorithms](non)
    * [Counting Sort](#count)
 5. [Implementation and Benchmarking](#imp)
10. [Conclusion](#con)
11. [Bibliography](#bib)
    

<a name="intro"></a>
## Introduction:

<a name="c"></a>
### Concept of Sorting

Sorting is a technique of arranging and rearranging a collection of items to some pre-defined ordering rule. This process makes it easier to understand, analyze or visualize the data. Today, we have an inconceivably large amount of data due to electronic storage media. In fact it is estimated that over 90% of data in the world has been created since 2016. 

<a name="r"></a>
### Relevance of sorting algorithm to the modern world:

* Phone numbers stored in mobile device which are normally sorted alphabetically by name. This is important as it allows numbers to be accessed easily and efficiently.
* How products are displayed on e-commerce sites
* Perhaps the most prominent sorting algorithm is PageRank which is used by Google to rank websites based on number of links to the website, among other features. [1]


<a name="his"></a>
### Sorting Algorithm Timeline:

 <p align="center">
   <img src="https://github.com/Roisin-Fallon/Sorting_Algorithms/blob/master/Timeline.PNG" title="Sorting Algorithm timeline" > 
 </p>
 
 <a name="sp"></a>
### Space Complexity:
 
- Space Complexity is a function describing the total space used by the algorithm to compete its execution in terms of input size and auxiliary space. 

<p align="center">
   <b> <i> Space Complexity = Auxiliary Space + Input Size </i> </b> </p>
   
- Auxiliary space refers to the extra or temporary space that is required by the algorithm during its execution. 
- An algorithm requires space during execution for the following for 3 reasons:

  - Instruction Space refers to the the amount of memory used to save the compiled version of instructions. The space is fixed but varies depending on the number of lines of code in the program.  
   - Environmental Stack- At times an algorithm(function) may be called inside another algorithm(function). If this occurs, the current variables are pushed onto the system stack, where they wait for further execution and then the call to the inside algorithm (function) is made. Essentially it is the space needed to store the environment information to resume the suspended function.    
    - Data Space - is the amount of space needed to store all the variables and constants values. 

Note while calculating Space Complexity of an algorithm normally Data Space is used while the others (Instruction Space and Environmental Stack) are ignored. [15]

 
 
 <a name="time"></a>
### Time Complexity:
 
 To analysis the time complexity of an algorithm, the number of operations and arithmetic operations are determined. Time complexity of an algorithm represents the amount of time required by the program to run until completion and is the most popular metric for calculating time complexity is Big O notation. Time complexity is measured in terms of the number of operations an algorithm uses.

<b> Asymptotic Notations </b>

Asymptotic Notations are languages that allow us to analyze an algorithm’s running time by identifying its behavior as the input size for the algorithm increases. This is also known as an algorithm’s growth rate [9].

The 3 asymptotic notations that will be discussed in terms of time complexity:

<b> Big Oh (O) – Upper Bound </b> 

Big O represents the maximum amount of resources in terms of space and time that an algorithm would require to run. It provides an upper bound on the number of operations an algorithm uses to solve a problem with input of a particular size. Describes the complexity of an algorithm in the worst case. It tells us that a function grows slower or at least as slow as another. 

<b> Big Omega (Ω) – Lower Bound </b>

Omega represents the minimum amount of resources in terms of space and time that an algorithm would require to run. It describes the complexity of an algorithm in the best case.  It tells us that a function grows at least as fast as another. 

<b> Big Theta (Θ)- Average Bound </b>

Theta represents the functions that lie in both O  and Ω expression. It describes the complexity of an algorithm in the average case. It is usually much more difficult to determine the average case time complexity of an algorithm. It represents the average number of operations an algorithm uses to solve a problem over all inputs of a particular size [14].
[13]

There is a strong correlation between run time of a sorting algorithm and the number of inversions in the input array, where the inversion number relates to one measure of how far it is from being sorted [11].

The different sorting algorithms are a perfect showcase of how algorithm design can have such a strong effect on program complexity, speed, and efficiency [10].

<b> There are 4 desirable properties for a sorting algorithm: </b>

1. Stable sorting algorithms retains the relative order of elements with equal keys. Using an unstable sorting algorithm changes the relative order of elements with equal keys [12].

Stable Sort              |  Unstable sort
:-------------------------:|:-------------------------:
![Stable Sort](https://www.tutorialspoint.com/data_structures_algorithms/images/stable_sort.jpg) |![Unstable Sort](https://www.tutorialspoint.com/data_structures_algorithms/images/unstable_sort.jpg)

2. In-place sorting (Internal sorting): uses only a fixed additional amount of working space, independent of the input size. Algorithms within this category: Selection Sort, Insertion Sort, Bubble Sort, Quick Sort. Not-in place (External Sorting): algorithms that require additional working memory, the amount of which is often related to the input size. Algorithms within this category: Merge Sort. This is a desirable property if you are concerned about the availability of space.
3. Run time efficiency (Best, Average and Worst case)
4. Suitability – properties of sorting algorithm are well matched to the class of input instances which are expected (determine the advantages and disadvantages of each algorithm when choosing them). 


<a name="par"></a>
### Comaprasion Sort:

Comparison Sorting Algorithm characterizes data using comparison operations only to determine which of  the two elements will appear first in a sorted list. Comparison sort make no assumptions and compares every element in the array with each other. Comparison sorts are widely applicable to diverse types of data input however no algorithm that sorts by comparison can do better than <i> nlogn </i> in the average or worst case. [11]

Within the comparasion sorting algorithms it can be further classified into:
   * Simple Comparasion Sorting Algorithms 
   
        * Bubble Sort
        * Selection Sort 
        * Insertion Sort
        
   * Efiiceint Comparasion Sorting Algorithms 
   
      * Merge Sort
      * Quicksort
      * Heap Sort
  

<a name="bub"></a>
### Bubble Sort:

Bubble sort is the simplest sorting algorithm. It gets its name from the way larger values in  an array “bubble up”  end as the numbers are sorted. 

<p align="center">
   <img src="https://upload.wikimedia.org/wikipedia/commons/0/06/Bubble-sort.gif"> 
</p>

<b> Bubble Sort Procedure: </b>
<i>
- Compares the first 2 elements in the array, it swaps the numbers if they are out of order and repeats this process  for each adjacent elements to the end of the array. It then starts back at the first 2 elements in the array until no swaps occur in the last pass [4]
- Repeatedly compares each element (except the final one) with the neighbour to the right,. It swaps the numbers if they are out of order. This number is placed at the end s now fixed in place. This process is repeated until there are no more swaps required
</i>

<b> Advantages: </b>
1. Easy to understand and implement – Hence is often used as a teaching tool
2. In place – no additional temporary storage required
3. Minimal space requirement
4. Performs well when the array is already sorted, best case O(n) as it only takes one iteration to detect collection is already sorted. [3]

<b> Disadvantages: </b>
1. Worst and Average case is very slow O(n2) because the entire array needs to be iterated for every element and hence it does not perform well in large unordered datasets. 

<i> Hence Bubble sort is not as practical or efficient as other algorithms dealt with in this project and hence is rarely used in the real world. </i>

<h4><i> Bubble Sort Python Code</i></h4>
   
      # Adapted from: https://www.geeksforgeeks.org/bubble-sort/
      def bubbleSort(alist):              
          n = len(alist)
          for i in range(n):                                                   # Traverse through all elements in the array
              for j in range(0, n-i-1):                                        # Last i elements are already in place
                  if alist[j] > alist[j+1]:                                    # Swap if the element is greater than the next element
                      alist[j], alist[j+1] = alist[j+1], alist[j]


   
<a name="in"></a>
### Insertion Sort:

Insertion sort is a comparison based sorting algorithm which is  faster than its counterparts (bubble sort and selection sort). An analogy is often made to the method used by card players to sort cards in their hands. 

<p align="center">
   <img src="https://upload.wikimedia.org/wikipedia/commons/9/9c/Insertion-sort-example.gif"> 
</p>

<b> Insertion Sort Procedure: </b>

<i>
   
* Set “key” as the element at index 1 (left of the array). Move any elements  to the left that are > the “key” right by one position, and insert the “key”. 
   
* Set “key” as the element at index 2 (left of the array). Move any elements  to the left that are > the “key” right by one position, and insert the “key”. 

* …..

* Set “key” as the element at index n-1. Move any elements  to the left that are > the “key” right by one position, and insert the “key”. [2]
</i> 

<b> Advantages: </b>

1. Easy to implement 
2. Efficient for small datasets 
3. Best case occurs if an array is already sorted Ω(n) as it has no inversions 
4. Most efficient of the simple sorting algorithms (bubble sort and selection sort),  best case would be if the array is nearly sorted time complexity is n + d (n refers to the numbers in the array and d refers to the number of inversions)
5. Stable retains the relative order of elements with equal keys 
6. In place sorting requires O(1), minimal space requirements

<b> Disadvantages: </b>

1. Less efficient on larger data sets as n2 steps required for every n elements to be sorted in the array. 
2. Worst case O(n2) would be if no numbers in the array (reverse sorted input) are sorted. [5]

<
<h4><i>Insertion Sort Python Code </i></h4>

      # Adapted from: https://www.geeksforgeeks.org/python-program-for-insertion-sort/

      def insertionSort(alist):                                   # Function to do insertion sort
           for i in range(1,len(alist)):                          # Start for loop at second element (index 1), assume the first element is sorted
              key=alist[i]                                        # Next element inserted into sorted section of array
              position = i -1                                     # Last element we are going to compare with

      # Comparing the current element with the sorted position and swapping 
              while position>=0 and key < alist[position]:        # Move the key as long as it is less than the previous item in the array
                  alist[position +1]=alist[position]              # Move the last element compared on step above to make room for key
                  position -= 1                                   # The next item to compare
              alist[position+1]=key              

<a name="quick"></a>
### Quick Sort:

Quicksort is a divide and conquer algorithm which is comparable to merge sort. Although it is slightly more complicated, it is usually significantly faster than merge sort and does not require the use of additional memory.

<p align="center">
   <img src="https://upload.wikimedia.org/wikipedia/commons/9/9c/Quicksort-example.gif"> 
</p>

<i>
<b> Quicksort Procedure has 3 basic steps:</b>

1. Pivot selection: select an element that is the designated “pivot” from the array
2. Partitioning: reorder the array so that all elements < the pivot are to the left while all elements >= the pivot are moved to the right. 
3. Recursion: step 1 and step 2 are applied recursively to the subsequent sub arrays. </i> [6]

<b> Advantages: </b>  [7;8]

1. Very fast for both: Average and Best case <i> (n log n) </i>. The best case occurs where both arrays are the same length i.e when the partition process always picks the middle element as pivot. [7;8]
2. Able to deal with larger datasets

<b> Disadvantages: </b>
1. Worst case is very slow n2 although this is extremely rare that it reaches its worst case complexity. Worst case can occur if the maximum or minimum element is always chosen as pivot.  
2. Bad implementation of the worst case may cause infinite looping and stack overflow
3. Tricky to implement and debug
4. Bubble sort is more efficient if array is already sorted

<b> <i> Since the partition method depends on the pivot it can be seen that the value of the pivot will affect the performance of Quick Sort. </i> </b>


<h4><i> Quicksort Python Code </i></h4>
 
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




<a name="merge"></a>
### Merge Sort:

Quicksort is a divide and conquer recursive algorithm. 

<p align="center">
   <img src="https://upload.wikimedia.org/wikipedia/commons/c/cc/Merge-sort-example-300px.gif"> 
</p>

<i>
   
* If only one element is in the array it is already sorted and return
* Splits an unsorted list recursively in half into n sublists, each comprising of a singular elements (list of 1 element is supposed sorted) 
* Merge sublists two at a time to give a new sorted sublist until it includes all elements now in a single sorted array. [6]
</i>

<b> Advantages:</b> 

1. Stable sort
2. Excellent choice if predictable runtime is important 
3. Good all round performance as its best, worst and average time complexity is <i> O(n log n) </i>

<b> Disadvantages: </b>

1. Requires extra memory, proportional to the number in the array O(n). This can slow down sorting of large datasets as it holds the sublists 


<h4><i> Merge Sort Python Code</i></h4> 

       # Adapted from: https://www.geeksforgeeks.org/merge-sort/

      def mergeSort(alist):

          #print("Splitting ",alist)
          if len(alist)>1:
              mid = len(alist)//2                  # Find the middle of the array

              L = alist[:mid]                         # Divide the list elements into 2 halfs: right and left
              R = alist[mid:]

              mergeSort(L)                            # Sort the left half
              mergeSort(R)                            # Sort the right half

              i = j = k = 0
              
              # Copy data to temp arrays L[] and R[] 
              
              while i < len(L) and j < len(R):
                  if L[i] < R[j]:
                      alist[k] = L[i]
                      i+=1
                  else:
                      alist[k]=R[j]
                      j+=1
                  k+=1

               # Checking if any element was left 

              while i < len(L):                        
                  alist[k]=L[i]
                  i+=1
                  k+=1

               # Checking if any element was right

              while j < len(R):                        
                  alist[k]=R[j]
                  j+=1
                  k+=1

<a name="non"></a>
## Non - Comparasion Sorting Algorithms:

Non-comparison sorts can be distinguished from comparison sorts as they make assumptions about data which eliminates the need to compare elements against each other (if we know data falls into a certain range). By making such assumptions it is possible to have a minimum sorting time of <i>O(n) </i> as elements must be examined at least once. 
Non-comparison sorts:

   * Counting Sort,
   * Bucket Sort 
   * Radix Sort


<a name="count"></a>
### Counting Sort:

Counting sort is a non–comparison based sorting algorithm. based on keys between a specific range.  Counting sort technique  is based on key values (integer sorting). Counting sort establishes the number of unique objects and uses arithmetic to calculate the position of each object in the output sequence. 

A number of assumptions are made about the type of input: 

  * Assume each of the n input elements has a positive integer key with a range of 0 to  k (if you are using zero indexing keys are in the range [0,….., k-1]).  n refers to the number of elements and k refers to the highest value element. 
[6]

<p align="center">
   <img src="https://camo.githubusercontent.com/02f9a6cfab70c3bdc81dda16112638071b688710/68747470733a2f2f312e62702e626c6f6773706f742e636f6d2f2d785071796c6e67714153592f574c47713370396e3976492f414141414141414141484d2f4a48647458416b4a593877597a444d4258787161726a6d687050684d3075384d41434c63422f73313630302f526573756c74417272617943532e676966"> 
</p>
<i>
   
1. Establish the key range  k in the input array (if currently unknown)
2. Initialise an array count of size k ,which will be used to count the number of times that each key value appears in the input instance.
3. Initialise an array result of size n, which will be used to store the sorted output.
4. Iterate through the input array, and record the number of times each distinct key values occurs in the input instance.
5. Construct the sorted result array, based on the histogram of key frequencies stored in count. Refer to the ordering of keys in input to ensure that stability is preserved.
</i>
<b> Advantages: </b>

1. Counting sort is stable (if implemented in the correct manner)
2. Effective only when the variation in keys is not significantly greater than the number of items, otherwise it can increase space complexity.
3. It is only suitable for direct se where the variation in keys is not significantly greater than the number of items.
4. Best, average and worst-case time complexity of <i> n + k </i>,  space complexity is <i> n + k </i>.

<b> Disadvantages: </b>

1. It can only be implemented on integers, which makes it less applicable then comparative sorting algorithms
Space complexity <i> O(n +k) </i>


<h4><i>Counting Sort Python Code </i></h4>

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
          return array



<a name="imp"></a>
## Implementation and Benchmarking:

Benchmarking also known as posteriori analysis which evaluates efficiency empirically (using experiments). The relative performance is analyzed by comparing  the actual measurements that has been collected during experiment for the algorithms implemented. It is a measure of the real world performance of your algorithm but is affected by various hardware and software factors which include:

  * System architecture
  * CPU design
  * Choice of Operating System 
  * Background processes
  * Energy saving 
  * Performance enhancing technologies

Hence it is recommended that multiple runs are performed using same experimental setup to establish an average expected performance. 
Benchmarking can be used to verify the priori analysis (theory) of algorithms [16].

To benchmark the algorithms I used 15 input sizes and used 3 separate random arrays ranges. 

*	Range 0 – 20000
*	Range 0 – 50000
*	Range 0 – 100000



  
 <b><i> Generate Array with random numbers using randint from Pythons random library</b></i>
  
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

Please note the above code refers to one of the 3 arrays created, the code for the other arrays are included in this project HERE.  


<a name="con"></a>
## Conclusion:
![Algorithm Sorting Property Summary](https://github.com/Roisin-Fallon/Sorting_Algorithms/blob/master/summary.png)
<p align="center">
   <img src="https://res.cloudinary.com/practicaldev/image/fetch/s--ark_FZG1--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/1omv0tmikzeaj24z8ps2.jpeg"> 
</p>
 <p align="center">
   <img src="https://github.com/Roisin-Fallon/Sorting_Algorithms/blob/master/Tables/Table1.PNG" title="Table for range 0 - 20000" > 
 </p>
 
 <p align="center">
   <img src="https://github.com/Roisin-Fallon/Sorting_Algorithms/blob/master/Graph/Graph1.PNG" title="Graphical representation of sorting algorithms: input range 0 - 20000" > 
 </p>
 


In terms of time complexity it is clear from the graph above that Bubble sort is the slowest of the algorithms that were selected in this project. This is in keeping with the expectation from the table above as the average case is <i> n2 </i>, where n refers to the number of items to sort. As stated earlier the simplicity of this algorithm makes it ideal as a teaching tool, however it is not a realistic for it to be used in real life. 

 <p align="center">
   <img src="https://github.com/Roisin-Fallon/Sorting_Algorithms/blob/master/Tables/Table2.PNG" title="Sorting Algorithm timeline" > 
 </p>
 
  
 <p align="center">
   <img src="https://github.com/Roisin-Fallon/Sorting_Algorithms/blob/master/Graph/Graph2.PNG" title="Graphical representation of sortig algorithms: input range 0 - 50000" > 
 </p>
  
 
Insertion Sort performs significantly better than Bubble sort but significantly worse than the remaining algorithms. This is in keeping with the theory that insertion sort performs better than its simple sort counterparts (Bubble Sort and Insertion Sort). However, the time efficiency is inferior to the efficient comparison based sorting algorithms (Merge Sort and Quicksort). Hence, in the second graph when the input size was increased to 50000 insertion sort can easily be separated. It is important to be aware that insertion sort can be useful in certain circumstances e.g. when they are a small number of items or when the items are mostly sorted. 

 <p align="center">
   <img src="https://github.com/Roisin-Fallon/Sorting_Algorithms/blob/master/Tables/Table3.PNG" title="Table for range 0 - 100000" > 
 </p>
  
 <p align="center">
   <img src="https://github.com/Roisin-Fallon/Sorting_Algorithms/blob/master/Graph/Graph3.PNG" title="Graphical representation of sortig algorithms: input range 0 - 100000" > 
 </p>

In the third and final graph input size is increased to 100000. Please note I omitted both bubble and insertion sort from this graph which allowed a clearer view of the difference between the efficient comparison based sorting algorithms and the non-comparison based sorting algorithm (counting sort). Both merge and insertion sort employ a divide and conquer approach with merge sort performing the better of the two. This matches the expectation that as the input size increases merge sort is the superior algorithm. Interestingly from the above table, in the worst case (Big O) scenario Quick Sort is <i> n2 </i>  and Merge Sort  is <i> n log n </i>. Merge Sort is an excellent choice if predictable runtime is important as its best, worst and average time complexity is <i> O (n log n) </i>. 

Finally counting sort performed the best of the five algorithms selected for this project with a potential runtime of <i> n+k  </i>  in the best, worst and average case, (where n refers to the input size and  each item has a non-negative integer key,  with a range of k). However it is important to be aware that this is not as widely as applicable as comparison sorts.  

In completing this project it is clear that no single algorithm can be isolated as the best in all instances when sorting input data as it can be affected by a number of factors e.g. input size, level of sorting etc.
Hence the advantages and disadvantages of each algorithm (as outlined in this project) should be weighed up before making your selection. 

<a name="bib"></a>
## Bibliography:
1. A brief history of algorithms (and why it's so important in automation, machine learning, and everyday life). [ONLINE] Available at: https://e27.co/brief-history-algorithms-important-automation-machine-learning-everyday-life-20161207/. [Accessed 18 April 2019].
2. P.Mannion (2019) Week 9: Sorting Algorithms Part 2, Galway-Mayo Institute of Technology
3. Karuna Sehgal. 2019. An Introduction to Bubble Sort – Karuna Sehgal – Medium. [ONLINE] Available at: https://medium.com/karuna-sehgal/an-introduction-to-bubble-sort-d85273acfcd8. [Accessed 2 May 2019].
4. Wikipedians & Creutzburg, Reiner & Knackmuß, Jenny. (2013). Lecture Notes - Algorithms and Data Structures - Part 4: Searching and Sorting. 10.13140/2.1.5158.0486.  [ONLINE] Available at:https://www.researchgate.net/publication/259398088_Lecture_Notes_-_Algorithms_and_Data_Structures_-_Part_4_Searching_and_Sorting/citation/download. [Accessed 2 May 2019].
5. What are the advantages and disadvantages to an insertion sort? - Quora. 2019. What are the advantages and disadvantages to an insertion sort? - Quora. [ONLINE] Available at: https://www.quora.com/What-are-the-advantages-and-disadvantages-to-an-insertion-sort. [Accessed 6 May 2019].
6.  P.Mannion (2019) Week 10: Sorting Algorithms Part 3, Galway-Mayo Institute of Technology
7. Sorting Algorithms in Software Development | RoBa's World. 2019. Sorting Algorithms in Software Development | RoBa's World. [ONLINE] Available at: https://www.robasworld.com/sorting-algorithms/. [Accessed 11 May 2019].
8. GeeksforGeeks. 2019. QuickSort - GeeksforGeeks. [ONLINE] Available at: https://www.geeksforgeeks.org/quick-sort/. [Accessed 11 May 2019].
9. Meet Zaveri. 2019. An intro to Algorithms: Searching and Sorting algorithms. [ONLINE] Available at: https://codeburst.io/algorithms-i-searching-and-sorting-algorithms-56497dbaef20. [Accessed 11 May 2019].
10. George Seif. 2019. A tour of the top 5 sorting algorithms with Python code. [ONLINE] Available at: https://medium.com/@george.seif94/a-tour-of-the-top-5-sorting-algorithms-with-python-code-43ea9aa02889. [Accessed 11 May 2019].
11. P.Mannion (2019) Week 8: Sorting Algorithms Part 1, Galway-Mayo Institute of Technology [11]
12. Sorting Algorithms in Software Development | RoBa's World. 2019. Sorting Algorithms in Software Development | RoBa's World. [ONLINE] Available at: https://www.robasworld.com/sorting-algorithms/. [Accessed 11 May 2019].
13. Time Complexity of Algorithms | Studytonight. 2019. Time Complexity of Algorithms | Studytonight. [ONLINE] Available at: https://www.studytonight.com/data-structures/time-complexity-of-algorithms. [Accessed 11 May 2019].
14. Algorithms Chapter 3 [ONLINE] Available at: https://player.slideplayer.com/32/9926197/#. [Accessed 11 May 2019].
15. Space Complexity of Algorithms | Studytonight. 2019. Space Complexity of Algorithms | Studytonight. [ONLINE] Available at: https://www.studytonight.com/data-structures/space-complexity-of-algorithms. [Accessed 04 May 2019].
16. P.Mannion (2019) Week 12: Benchmarking Algorithms in Python, Galway-Mayo Institute of Technology
