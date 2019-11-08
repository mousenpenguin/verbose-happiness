Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def heapify(data, element,i ):
    biggest = i
    left = 2 * i + 1
    right = 2 * i + 2
 
    if left < element and data[i] < data[left]:
        biggest = left
 
    if right < element and data[biggest] < data[right]:
        biggest = right
 
    if biggest != i:
        data[i],data[biggest] = data[biggest],data[i]
 
        heapify(data, element, biggest)

        
>>> def heapSort(data):
    element = len(data)
 
    for i in range(element, -1, -1):
        heapify(data, element, i)
 
    for i in range(element-1, 0, -1):
        data[i], data[0] = data[0], data[i]
        heapify(data, i, 0)

        
>>> a=[2,5,7,3,5,8,4,9,1]
>>> heapSort(a)
>>> print(heapSort)
<function heapSort at 0x03AAB588>
>>> print(a)
[1, 2, 3, 4, 5, 5, 7, 8, 9]
>>> 
