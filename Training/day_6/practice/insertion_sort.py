def insertion_sort(array):
   
    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1

        while j >= 0 and array[j] > key_item:
            # Shift the value one position to the left
            # and reposition j to point to the next element
            # (from right to left)
            array[j + 1] = array[j]
            j -= 1

        # When finish shifting the elements, position `key_item` in its correct location
        array[j + 1] = key_item

    return array

array = [19,2,31,45,6,11,121,27]
insertion_sort(array)
print(array)