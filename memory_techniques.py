# KEY TECHNIQUES
# Write out the available information, problem solving steps & pseudo code
# Determine which DS can be used, or can be created for use
# What useful information is known about this DS?
# Determine which algorithmic blueprint to use - if applicable
# If no blueprint, leverage hashing, indexing (including keeping track of)
#   and key built-ins like min/max/any/all/gen x/list comp


# RECURSION STRATEGY:
# 1) Draw out the problem / scenario a few layers deep & determine the base
#   case (use a table with the base case at the bottom)
# 2) Write the recursive function call, passing a parameter which shrinks the
#   input toward the base case - could be multiple params, one needs to shrink
# 3) Adjust the return value from the function call to accurately return up the
#   stack, use the table from 1) to understand value of params at this point

# REMEMBER: You can implement more logic instead of returning immediately
# there could be multiple base/ recursive cases based on other input params

class SortAlgorithms:

    def insertion_sort(self, unsorted):
        for idx, _ in enumerate(unsorted):
            curr = idx
            while curr > 0 and unsorted[curr] < unsorted[curr - 1]:
                unsorted[curr], unsorted[curr - 1] = (
                    unsorted[curr - 1], unsorted[curr])
                curr -= 1
        return unsorted

    def bubble_sort(self, unsorted):
        count = len(unsorted)
        for i in reversed(range(count)):
            swapped = False
            for j in range(i):
                if unsorted[j] > unsorted[j + 1]:
                    unsorted[j], unsorted[j + 1] = unsorted[j + 1], unsorted[j]
                    swapped = True
                if not swapped:
                    return unsorted
        return unsorted

    def selection_sort(self, unsorted):
        count = len(unsorted)
        for i in range(count):
            min_index = i
            for j in range(i, count):
                if unsorted[j] < unsorted[min_index]:
                    min_index = j
            unsorted[i], unsorted[min_index] = unsorted[min_index], unsorted[i]
