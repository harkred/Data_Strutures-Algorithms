def insertion_sort(lst):
    l=len(lst)
    for i in range(1, l):
        key=i
        for j in range(0, key):
            if lst[key]<lst[j]:
                lst.insert(j, lst[key])
                lst.pop(key+1)
    return lst
    
lst=[5, 3, 7, 2, 1]
print(insertion_sort(lst))
