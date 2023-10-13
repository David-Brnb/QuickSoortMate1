# arreglo = [7,8,1,-3,5,10,21]
# arreglo = [7, 5, 1, -3] 
# arreglo = [5,5,4]
# arreglo = [5,5,5,5,5,5]
arreglo = [5,4,3,2,1]

#   Inercambia valores
def swap(arr, a,b):
    arr[a],arr[b] = arr[b],arr[a]

#   "Ordena"el arreglo
def quickSort(arr):
    if len(arr) <=2:
        return arr

    count = 0

    while True:
        if count == len(arr)-1:
            return arr
        if arr[count] < arr[count+1]:
            pivot = arr[count+1]
            m=count+1
            break

        elif arr[count] > arr[count+1]:
            swap(arr, 0, count+1)
            
            pivot = arr[count+1]
            m=count+1
            break
        count += 1

    i = m+1
    j = len(arr)-1

    while i < j:
        if arr[i] >= pivot and arr[j] < pivot:
            swap(arr, j, i)

        i+=1
        j-=1
    
    if i >= len(arr): i-=1

    k=i
    
    if arr[k] < arr[m]: 
        swap(arr, m, k)

    list1 = arr[:k]
    list2 = arr[k:]

    print(list1, list2)

    return quickSort(list1) + quickSort(list2)

    



print(quickSort(arreglo))

