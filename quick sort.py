def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]

    less = [x for x in array[1:] if x <= pivot]
    greater = [x for x in array[1:] if x > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)  
