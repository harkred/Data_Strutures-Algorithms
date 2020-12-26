def merge(left, right):
    left_index, right_index=0, 0
    lst=[]
    while left_index<len(left) and right_index<len(right):
        if left[left_index]<right[right_index]:
            lst.append(left[left_index])
            left_index+=1
        else:
            lst.append(right[right_index])
            right_index+=1
            
    if left_index!=len(left):
        lst.extend(left[left_index:])
    else:
        lst.extend(right[right_index:])
    return lst
 
def merge_sort(lst):
    l=len(lst)
    if l<=1:
        return lst
    mid=l//2
    left=merge_sort(lst[:mid])
    right=merge_sort(lst[mid:])
    return merge(left, right)
        
lst=[71, 8, 98, 24, 1, 0, 23]
print(merge_sort(lst))
