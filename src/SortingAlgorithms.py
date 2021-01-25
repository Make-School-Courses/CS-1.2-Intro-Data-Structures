# Bubble Sort
# Code from Geek for Geeks

def bubble_sort(lst): 
	n = len(lst) 

	# Traverse through all list elements 
	for i in range(n-1): 
	# range(n) also work but outer loop will repeat one time more than needed. 

		# Last i elements are already in place 
		for j in range(0, n-i-1): 

			# traverse the list from 0 to n-i-1 
			# Swap if the element found is greater 
			# than the next element 
			if lst[j] > lst[j+1] : 
				lst[j], lst[j+1] = lst[j+1], lst[j] 



# Selection Sort
# Code from Educative

def selection_sort(lst):
  n = len(lst)
  for i in range(n):
    # Initially, assume the first element of the unsorted part as the minimum.
    minimum = i

    for j in range(i+1, n):
      if (lst[j] < lst[minimum]):
        # Update position of minimum element if a smaller element is found.
        minimum = j

    # Swap the minimum element with the first element of the unsorted part.     
    temp = lst[i]
    lst[i] = lst[minimum]
    lst[minimum] = temp
    
  return lst



# Insertion Sort
def insertion_sort(lst):
    for i in range(1, len(lst)):
        # Set key:
        key = lst[i]

        j = i - 1
        while j >= 0 and lst[j] > key:
            # Swap:
            lst[j + 1] = lst[j]
            lst[j] = key
            
            # Decrement 'j':
            j -= 1

    return lst


array = [5, 2, 12, 12, 1]
print("Original array: %s" % array)
print("Sorted array: %s" % insertion_sort(array))






# Merge Sort
def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]

        # Recursive call on each half
        merge_sort(left)
        merge_sort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              # The value from the left half has been used
              lst[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                lst[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst[k]=right[j]
            j += 1
            k += 1

	
	
	
	
# Quick Sort

def quick_sort(lst):

    elements = len(lst)
    
    #Base case
    if elements < 2:
        return lst
    
    current_position = 0 #Position of the partitioning element

    for i in range(1, elements): #Partitioning loop
         if lst[i] <= lst[0]:
              current_position += 1
              temp = lst[i]
              lst[i] = lst[current_position]
              lst[current_position] = temp

    temp = lst[0]
    lst[0] = lst[current_position] 
    lst[current_position] = temp #Brings pivot to it's appropriate position
    
    left = quick_sort(lst[0:current_position]) #Sorts the elements to the left of pivot
    right = quick_sort(lst[current_position+1:elements]) #sorts the elements to the right of pivot

    lst = left + [lst[current_position]] + right #Merging everything together
    
    return lst

