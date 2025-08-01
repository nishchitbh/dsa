from sort_algo.array import generate_array

def sort(array):
    for i in range(1, len(array)):
        selected_card = array[i]
        j = i - 1
        while j > -1 and array[j] > selected_card:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = selected_card
    return array


def runner():
    array = generate_array(25).copy()
    sorted_array = sort(array)
    return sorted_array


print(runner())