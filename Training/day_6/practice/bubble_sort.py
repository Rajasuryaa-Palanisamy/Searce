def bubble_sort(array):
    n = len(array)

    for i in range(n):
        # Create a flag that will allow the function to terminate early if there's nothing left to sort
        already_sorted = True

        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                # If the item you're looking at is greater than its adjacent value, then swap them
                array[j], array[j + 1] = array[j + 1], array[j]

                already_sorted = False

        if already_sorted:
            break

    return array

array = [19,2,31,45,6,11,121,27]
bubble_sort(array)
print(array)