from sort_algo.array import generate_array

def merge_sort(array):
    if len(array)<=1:
        return array
    mid = len(array)//2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i+=1
        else :
            merged.append(right[j])
            j+=1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
    
def runner():
    array = generate_array(10)
    sorted_array = merge_sort(array)
    print(sorted_array)
    
if __name__ == "__main__":
    runner()