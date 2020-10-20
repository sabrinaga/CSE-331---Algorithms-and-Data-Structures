def merge_sort(unsorted, threshold, reverse):
    '''function which merge sorts depending on a threshold, and
    reverse sorts'''
    if len(unsorted) < 2:
        return unsorted
    elif len(unsorted) > threshold:
        mid = len(unsorted) // 2
        sublist1 = unsorted[0:mid]
        sublist2 = unsorted[mid:len(unsorted)]
        sublist1 = merge_sort(sublist1, threshold, reverse)
        sublist2 = merge_sort(sublist2, threshold, reverse)
        unsorted = merge(sublist1, sublist2, reverse) 
        #merge returns sorted list, so unsorted now becomes sorted
    else:
        unsorted = insertion_sort(unsorted, reverse)
    return unsorted

def merge(first, second, reverse):
    '''merge the lists back together'''
    merged_list = [] #declaring new list, will be like S in example
    i = j = 0
    if reverse == False:
        while i < len(first) and j < len(second):
            if first[i] < second[j]:
                merged_list.append(first[i])
                i += 1
            else:
                merged_list.append(second[j])
                j += 1
        while i < len(first):
            merged_list.append(first[i])
            i += 1
        while j < len(second):
            merged_list.append(second[j])
            j += 1
        return merged_list
    else:
        while i < len(first) and j < len(second):
            if first[i] > second[j]:
                merged_list.append(first[i])
                i += 1
            else:
                merged_list.append(second[j])
                j += 1
        while i < len(first):
            merged_list.append(first[i])
            i += 1
        while j < len(second):
            merged_list.append(second[j])
            j += 1
        return merged_list

def exchange(unsorted, i, j):
    '''Make swaps for insertion_sort'''
    unsorted[i], unsorted[j] = unsorted[j], unsorted[i]

def insertion_sort(unsorted, reverse):
    ''' Sorting algorithm, which is faster than merge at given
    threshold'''
    size = len(unsorted)
    if reverse is False:
        for i in range(1, size):
            j = i
            while (j > 0) and (unsorted[j] < unsorted[j - 1]):
                exchange(unsorted, j, j - 1)
                j -= 1
    else:
        for i in range(1, size):
            j = i
            while (j > 0) and (unsorted[j] > unsorted[j-1]):
                exchange(unsorted, j, j-1)
                j -= 1
    return unsorted
    
