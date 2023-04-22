## Python Bubble Sorting

This repository contains a simple Python implementation of the bubble sorting algorithm.

The idea behind bubble sort is to repeatedly swap adjacent elements in a list until they are sorted. The algorithm gets its name from the way smaller elements "bubble" to the top of the list.

### How it works
![Bubble Sort Example](https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif)

As you can see in the animation above, the bubble sort algorithm starts by comparing the first two elements of the list. If the first element is greater than the second element, the algorithm swaps them. Then it compares the second and third elements, and so on, until it reaches the end of the list. At this point, the largest element is guaranteed to be at the end of the list. 

The algorithm then repeats the process for the remaining elements of the list (i.e., all elements except the last one). After each iteration, the largest remaining element "bubbles up" to its correct position in the sorted list.

### Usage
The `bubble_sort` function defined in `bubble_sort.py` takes a list of numbers as its input and returns a sorted list. 

```python
from bubble_sort import bubble_sort

unsorted_list = [5, 3, 8, 6, 7, 2]
sorted_list = bubble_sort(unsorted_list)
print(sorted_list)
```

### Output:
```python
[2, 3, 5, 6, 7, 8]
```

## Installation:

You can install this package using pip:

```sh
pip install python-bubble-sort
```

### Author
This implementation was created by Isaac Lyne.

### License
This project is licensed under the MIT License - see the LICENSE file for details.
