def quicksort(list):
    if len(list) < 2:
        return list
    else:
        pivot = list[0] # 选择基准值
        less = [i for i in list[1:] if i <= pivot] # 选出小于基准值的元素
        greater = [i for i in list[1:] if i > pivot] # 选出大于基准值的元素
    
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([1, 3, 5, 2, 0, 8]))

