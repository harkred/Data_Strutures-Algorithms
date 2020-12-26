def bubble_sort(lst):
    l=len(lst)
    for i in range(l):
        for j in range(l-i):
            try:
                if lst[j]>lst[j+1]:
                    lst[j], lst[j+1]=lst[j+1], lst[j]
                else:
                    continue
            except Exception as e:
                pass
    return lst

lst=[22, 11, 4, 55, 23, 1]
print(bubble_sort(lst))

