Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def merge(left, right):
    final = []  
    l,m = 0,0
 
    while l<len(left) and m<len(right):
        if left[l] <= right[m]:
            final.append(left[l]) 
            l+=1
        else:
            final.append(right[m])  
            m+=1
    final += left[l:]
    final += right[m:]
    return final

>>> def mergeSort(array):
    if(len(array)<= 1): 
        return array

    mid = int(len(array)/2)
    left = mergeSort(array[:mid])
    right = mergeSort(array[mid:])
 
    return merge(left,right)

>>> a = [2,8,4,1,5]
>>> print(mergeSort(a))
[1, 2, 4, 5, 8]
>>> 
