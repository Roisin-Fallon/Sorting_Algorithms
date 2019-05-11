# Programming_and_Scripting_Project_2019


### Table of Contents

1. [ Introduction ](#intro)
    * [Concept of Sorting](#c)
    * [Relevance of sorting algorithm to the modern world](#r)
    * [History of algorithms ](#his)
2. [Simple Comparative Sorting Algorithms]
    * [Bubble Sort](#bub)
    * [Insertion Sort](#in)
3. [Efficient Comparative Sorting Algorithms]
    * [Quick Sort](#quick)
    * [Merge Sort](#merge)
4. [Non-comparative Sorting Algorithms]
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
### History of algorithms 
 <p align="center">
   <img src="              " title="Sorting Algorithm timeline" > 
 </p>
 
 
<a name="bub"></a>
### Bubble Sort:

Bubble sort is the simplest sorting algorithm. It gets its name from the way larger values in  an array “bubble up”  end as the numbers are sorted. 

<p align="center">
   <img src="https://upload.wikimedia.org/wikipedia/commons/0/06/Bubble-sort.gif"> 
</p>

<b> Bubble Sort Procedure: </b>
<i>
* Compares the first 2 elements in the array, it swaps the numbers if they are out of order and repeats this process  for each adjacent elements to the end of the array. It then starts back at the first 2 elements in the array until no swaps occur in the last pass [4]
* Repeatedly compares each element (except the final one) with the neighbour to the right,. It swaps the numbers if they are out of order. This number is placed at the end s now fixed in place. This process is repeated until there are no more swaps required
</i>

<b> Advantages: </b>
1. Easy to understand and implement – Hence is often used as a teaching tool
2. In place – no additional temporary storage required
3. Minimal space requirement
4. Performs well when the array is already sorted, best case O(n) as it only takes one iteration to detect collection is already sorted. [3]

<b> Disadvantages: </b>
1. Worst and Average case is very slow O(n2) because the entire array needs to be iterated for every element and hence it does not perform well in large unordered datasets. 

<i> Hence Bubble sort is not as practical or efficient as other algorithms dealt with in this project and hence is rarely used in the real world. </i>

<details><summary> Bubble Python Code</summary>
<p>
   
      # Code adapted from: https://www.geeksforgeeks.org/bubble-sort/
      def bubbleSort(alist):              
          n = len(alist)
          for i in range(n):                                                   # Traverse through all elements in the array
              for j in range(0, n-i-1):                                        # Last i elements are already in place
                  if alist[j] > alist[j+1]:                                    # Swap if the element is greater than the next element
                      alist[j], alist[j+1] = alist[j+1], alist[j]

</p>
</details>  
   
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

<details><summary> Insertion Python Code</summary>
<p>
   
</p>
</details>


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

<details><summary> Quick Python Code</summary>
<p>
   
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


</p>
</details>

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

<details><summary> Merge Python Code</summary>
<p>
 
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

</p>
</details>

<a name="count"></a>
### Counting Sort:

Counting sort is a non–comparison based sorting algorithm. based on keys between a specific range.  Counting sort technique  is based on key values (integer sorting). Counting sort establishes the number of unique objects and uses arithmetic to calculate the position of each object in the output sequence. 

A number of assumptions are made about the type of input: 

  * Assume each of the n input elements has a positive integer key with a range of 0 to  k (if you are using zero indexing keys are in the range [0,….., k-1]).  n refers to the number of elements and k refers to the highest value element. 
[6]

<p align="center">
   <img src="https://camo.githubusercontent.com/02f9a6cfab70c3bdc81dda16112638071b688710/68747470733a2f2f312e62702e626c6f6773706f742e636f6d2f2d785071796c6e67714153592f574c47713370396e3976492f414141414141414141484d2f4a48647458416b4a593877597a444d4258787161726a6d687050684d3075384d41434c63422f73313630302f526573756c74417272617943532e676966"> 
</p>

1. Establish the key range  k in the input array (if currently unknown)
2. Initialise an array count of size k ,which will be used to count the number of times that each key value appears in the input instance.
3. Initialise an array result of size n, which will be used to store the sorted output.
4. Iterate through the input array, and record the number of times each distinct key values occurs in the input instance.
5. Construct the sorted result array, based on the histogram of key frequencies stored in count. Refer to the ordering of keys in input to ensure that stability is preserved.

<b> Advantages: </b>

1. Counting sort is stable (if implemented in the correct manner)
2. Effective only when the variation in keys is not significantly greater than the number of items, otherwise it can increase space complexity.
3. It is only suitable for direct se where the variation in keys is not significantly greater than the number of items.
4. Best, average and worst-case time complexity of <i> n + k </i>,  space complexity is <i> n + k </i>.

<b> Disadvantages: </b>

1. It can only be implemented on integers, which makes it less applicable then comparative sorting algorithms
Space complexity <i> O(n +k) </i>

<details><summary> Counting Python Code</summary>
<p>

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

</p>
</details>

<a name="imp"></a>
## Implementation and Benchmarking:

<a name="con"></a>
## Conclusion:
![Algorithm Sorting Property Summary](https://github.com/Roisin-Fallon/Sorting_Algorithms/blob/master/summary.png)
<p align="center">
   <img src="https://res.cloudinary.com/practicaldev/image/fetch/s--ark_FZG1--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/1omv0tmikzeaj24z8ps2.jpeg"> 
</p>

<a name="bib"></a>
## Bibliography:
1. A brief history of algorithms (and why it's so important in automation, machine learning, and everyday life). [ONLINE] Available at: https://e27.co/brief-history-algorithms-important-automation-machine-learning-everyday-life-20161207/. [Accessed 18 April 2019].
2. P.Mannion (2019) Week 10: Sorting Algorithms Part 2, Galway-Mayo Institute of Technology
3. Karuna Sehgal. 2019. An Introduction to Bubble Sort – Karuna Sehgal – Medium. [ONLINE] Available at: https://medium.com/karuna-sehgal/an-introduction-to-bubble-sort-d85273acfcd8. [Accessed 2 May 2019].
4. Wikipedians & Creutzburg, Reiner & Knackmuß, Jenny. (2013). Lecture Notes - Algorithms and Data Structures - Part 4: Searching and Sorting. 10.13140/2.1.5158.0486.  [ONLINE] Available at:https://www.researchgate.net/publication/259398088_Lecture_Notes_-_Algorithms_and_Data_Structures_-_Part_4_Searching_and_Sorting/citation/download. [Accessed 2 May 2019].
5. What are the advantages and disadvantages to an insertion sort? - Quora. 2019. What are the advantages and disadvantages to an insertion sort? - Quora. [ONLINE] Available at: https://www.quora.com/What-are-the-advantages-and-disadvantages-to-an-insertion-sort. [Accessed 6 May 2019].
6.  P.Mannion (2019) Week 10: Sorting Algorithms Part 3, Galway-Mayo Institute of Technology
7. Sorting Algorithms in Software Development | RoBa's World. 2019. Sorting Algorithms in Software Development | RoBa's World. [ONLINE] Available at: https://www.robasworld.com/sorting-algorithms/. [Accessed 11 May 2019].
8. GeeksforGeeks. 2019. QuickSort - GeeksforGeeks. [ONLINE] Available at: https://www.geeksforgeeks.org/quick-sort/. [Accessed 11 May 2019].
