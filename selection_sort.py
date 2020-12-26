def selection_sort(lst):
    l=len(lst)
    for i in range(l):
        start=i
        for j in range(start, l):
            if lst[start]>lst[j]:
                lst[start], lst[j]=lst[j], lst[start]
    return lst

lst=[3, 2, 4, 1, 6, 5]
print(selection_sort(lst))      


