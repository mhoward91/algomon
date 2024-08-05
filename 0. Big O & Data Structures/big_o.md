# Big O Notation

#### Big O Notation is a framework used to judge which solutions are 'better' than others
#### Big O notation objectively describes code efficiency without the use of concrete units
#### Big O notation focuses on how time and space requirements scale with input growth
#### *A better solution minimises the time (duration) and space (memory) complexity*

### Big O Notation Rules
- Product Rule
    - If the Big O is the product of multiple terms, drop the constant terms
- Sum Rule
    - If the Big O is the sum of multiple terms, only keep the largest term

Example code: 

``` python
def list_average(numbers:list):
    sum = 0
    for number in numbers:
        sum += number
    return sum / len(numbers)

list_average([5, 6, 7, 8, 9, 10])
```

##### Time complexity Analysis of example code:
- define input: in this case, input is `n`, length of list
- look at code commands affected by input size, e.g. defining the sum as 0 isn't affected
- loops are code lines which are generally affected by input size
- only the sum += number line is affected
- constants are dropped so if there were 4 lines affected by input, `4n` would just become n
- **this function has an O(n) runtime, where n is the length of the input list**
- nested loops will have an O(n) of n ^ 2

##### Space complexity
- define input
- the number of variables required to store in memory and their size
- this does not include the input to the function itself
- so 3 variables unaffected by n yields an O(3 * n) = O(n)

### 7 Common complexity classes - in increasing order of complexity
#### Constant: O(1) (note arithmatic runs in constant time)
---
- The number of steps does not depend on input size
- Hashmap lookup, array access & update, pushing & popping to/from stack, appending to end of linked list
- Typically indicated by n > 10^9
#### Logarithmic: O(log(n))
---
- Number of steps can be expressed as a logarithm on the input size
- log(n) is how many times do you need to divide n by the base (assumed 2)
to get to the result, so n/2 operations are a good indicator of O(log(n)) complexity
- Binary search or variant, balanced binary search tree lookup, processing digits of a number
- Typically indicated by n > 10^8
**log(n) < n**
#### Linear: O(n)
---
- The number of steps depends exactly on input size
- looping through a linear data structure a constant amount of times
- Going through array/linked list to find an element, two pointers, tree/graph traversal, stack/queue, some greedy types
- printing is O(n)
- Typically n less than 10 ^ 6
#### O(k log(n))
---
- Heap push/pop K times (anything that seeks the "top K elements")
- K closest points, merge K sorted lists, binary search K times
- Typically n less than 10 ^ 6
#### Loglinear/Quasilinear - O(n*log(n))
---
- Has linear behaviour nested in log steps
- Sorting algorithms, divide & conquer
#### Polynomial: O(n^c), where c is a constant
---
- Includes O(n^2) - quadratic and O(n^3)
- nested loops, many brute force solutions
- Typically for n < 3000
#### Exponential: O(c^n), where the base is a constant
---
- commonly observed in recursive functions - doubling or tripling number of function calls
- e.g. one recursive function making two function calls each iteration would be O(2^n)
- Combinatorial problems, backtracking, subsets
- Typically for n < 20
#### Factorial: O(n!)
---
- Typically seen with a recursive call inside a for loop
- Combinatorial problems, backtracking, permutations
- Typicaly for n < 12

### A note on space complexity
- Recursive functions will have a space complexity equal to the stack depth = height of tree

##### Multiple inputs
- reference both inputs in notation, e.g. O(m + n)
- O(max(m, n)), where m, n are the string lengths
- O(n), where n is the length of the longer string

### Visualisation - 2^n/2 = O(2^n)

Value of n | No. of Nodes | Change in nodes | Total fn calls
--- | --- | --- | ---
8 | 1 | n/a | 31
6 | 2 | *2 | 15
4 | 4 | *2 | 7
2 | 8 | *2 | 3
0 | 16| *2 | 1

Therefore nodes (fn calls) increase exponentially so 2^n
Scaling of n is approx number of levels on the tree, so ~n/2
O(2^(n/2)) simplifies to O(2^n) 

![](https://miro.medium.com/max/1200/1*7p5XIlOv2uoxd_LFvPJ8qw.png)

