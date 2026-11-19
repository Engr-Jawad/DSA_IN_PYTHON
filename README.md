

Data Structures and Algorithms (DSA) in Python
Learning Goal
Learn DSA from zero, understand how each structure and algorithm works,
analyze its efficiency, and implement it in Python.

Learning style: Study one topic at a time. First understand the
idea, then trace an example by hand, then write Python code, and
finally analyze its time and space complexity.

Part 1: Foundations
1. What is Data?
Data means raw facts or values that a computer can store and
process.

Examples: - 25 --- an integer - "Jawad" --- a string - True --- a
Boolean value - [10, 20, 30] --- a collection of values

2. What is a Data Structure?
A data structure is a way of organizing and storing data so that we
can use it efficiently.

For example, if we store student marks:

marks = [75, 82, 91, 68]
A Python list keeps multiple values together and allows us to access
them by index.

Why do we need data structures?
To organize data.
To access data efficiently.
To insert, delete, and update values.
To solve problems in an organized way.
3. Types of Data Structures
A. Linear Data Structures
Elements are arranged in a sequence.

Examples: - Array - Linked List - Stack - Queue

B. Non-Linear Data Structures
Elements are not arranged in one simple sequence. They can form
hierarchical or network-like relationships.

Examples: - Tree - Graph - Heap - Trie

Part 2: Algorithm Fundamentals
4. What is an Algorithm?
An algorithm is a finite sequence of clear steps used to solve a
problem.

Example: Find the largest number in a list.

Assume the first number is the largest.
Compare it with every other number.
If a larger number is found, update the largest value.
Return the largest value.
5. Algorithm Analysis
Algorithm analysis helps us understand how efficient an algorithm is as
the input size grows.

We commonly analyze:

Time complexity: How the number of operations grows with input
size.
Space complexity: How the extra memory requirement grows with
input size.
6. Types of Complexity Analysis
Best Case
The minimum work an algorithm performs for an input of size n.

Average Case
The expected work across typical inputs of size n.

Worst Case
The maximum work an algorithm may perform for an input of size n.

7. Asymptotic Notations
Asymptotic notation describes how an algorithm's resource use grows as
input size becomes large.

Notation Meaning Simple interpretation

Big O --- O(...) Upper bound Often used to describe
worst-case growth

Big Omega --- Ω(...) Lower bound A lower bound on growth

Big Theta --- Θ(...) Tight bound Growth is bounded both
above and below
Common Time Complexities
From generally more efficient growth to less efficient growth:

Complexity Name Example

O(1) Constant Access a list element by index
O(log n) Logarithmic Binary search on sorted data
O(n) Linear Traverse a list
O(n log n) Linearithmic Merge sort
O(n²) Quadratic Two nested loops over the same input
O(2ⁿ) Exponential Some recursive subset problems
O(n!) Factorial Generate all permutations

Important: Big O is not the exact running time in seconds. It
describes how growth changes with input size.

Part 3: Searching Algorithms
8. Linear Search
Linear search checks elements one by one until it finds the target or
reaches the end.

Works on sorted and unsorted lists.
Best case: O(1)
Worst case: O(n)
Extra space for an iterative implementation: O(1)
9. Binary Search
Binary search repeatedly divides the search range in half.

Requires sorted data.
Best case: O(1)
Worst case: O(log n)
Iterative extra space: O(1)
Part 4: Sorting Algorithms
10. Bubble Sort
Bubble sort repeatedly compares adjacent elements and swaps them when
they are in the wrong order.

Example:

Initial:  [5, 2, 4, 1]
Pass 1:   [2, 4, 1, 5]
Pass 2:   [2, 1, 4, 5]
Pass 3:   [1, 2, 4, 5]
Sorted:   [1, 2, 4, 5]
Typical complexity: - Best case: O(n) with an early-stop
optimization. - Average case: O(n²). - Worst case: O(n²). - Extra
space: O(1).

11. Selection Sort
Selection sort repeatedly finds the smallest element in the unsorted
part and places it at the beginning of that part.

Example:

Initial:       [7, 2, 9, 4, 5]
Pass 1:        [2, 7, 9, 4, 5]
Pass 2:        [2, 4, 9, 7, 5]
Pass 3:        [2, 4, 5, 7, 9]
Sorted:        [2, 4, 5, 7, 9]
Typical complexity: - Best case: O(n²). - Average case: O(n²). -
Worst case: O(n²). - Extra space: O(1).

12. More Sorting Algorithms to Learn
Insertion Sort
Merge Sort
Quick Sort
Heap Sort
Counting Sort
Radix Sort
Part 5: Core Data Structures
Study each structure by understanding its operations, implementation,
and complexity.

13. Arrays and Python Lists
Learn: - Indexing and traversal - Searching - Insertion and deletion -
Updating elements - Two-dimensional lists

14. Linked Lists
Learn: - Nodes and pointers/references - Singly linked list - Doubly
linked list - Circular linked list - Insertion and deletion

15. Stack
A stack follows LIFO: Last In, First Out.

Main operations: - push --- add an item - pop --- remove the top
item - peek --- view the top item

Applications: undo operations, function calls, expression evaluation.

16. Queue
A queue follows FIFO: First In, First Out.

Main operations: - enqueue --- add an item - dequeue --- remove the
front item - front --- view the first item

Types: - Simple Queue - Circular Queue - Deque - Priority Queue

17. Hash Tables
Learn: - Key-value pairs - Hash functions - Collisions - Collision
handling - Python dictionaries and sets

18. Trees
Learn: - Tree terminology - Binary Trees - Binary Search Trees - Tree
traversal: preorder, inorder, postorder, level order - Balanced trees -
Heaps

19. Graphs
Learn: - Vertices and edges - Directed and undirected graphs - Weighted
and unweighted graphs - Adjacency list and adjacency matrix -
Breadth-First Search (BFS) - Depth-First Search (DFS) - Shortest-path
algorithms

Part 6: Problem-Solving Techniques
After learning the main structures, study:

Recursion
Backtracking
Two Pointers
Sliding Window
Divide and Conquer
Greedy Algorithms
Dynamic Programming
Part 7: Recommended Study Method
For every topic, follow these steps:

Understand: Explain the concept in your own words.
Visualize: Draw the data structure or algorithm.
Trace: Work through a small example by hand.
Implement: Write the Python solution yourself.
Analyze: Find time and space complexity.
Practice: Solve easy problems before moving to medium problems.
Review: Explain why your solution works.
Practice Checklist
Explain the concept without looking at notes.
Trace an example by hand.
Implement it in Python without copying.
Test normal, empty, and edge-case inputs.
Analyze best, average, and worst cases where relevant.
State time and space complexity.
Solve at least three practice problems.
Current Learning Progress
Based on the topics covered so far:


What is data?

What is a data structure?

Linear data structures

Non-linear data structures

Time complexity

Types of algorithm analysis

Selection sort

Bubble sort (currently learning)
Suggested Next Steps
Finish Bubble Sort and analyze its best, average, and worst cases.
Compare Bubble Sort with Selection Sort.
Learn Insertion Sort.
Practice Linear Search and Binary Search.
Continue to linked lists, stacks, and queues.
Quick Revision Questions
What is the difference between data and a data structure?
What is the difference between linear and non-linear data
structures?
What is an algorithm?
What is the difference between time complexity and space complexity?
What do O(1), O(n), and O(n²) mean?
Why does binary search require sorted data?
How does Selection Sort work?
How is Bubble Sort different from Selection Sort?
What is the difference between best-case and worst-case analysis?
Why do we analyze algorithms instead of only measuring their
execution time?
Keep practicing: Understanding the logic is more important than
memorizing code.





