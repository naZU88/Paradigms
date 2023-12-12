def Searching(l, n):
    first = 0
    last = len(l)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if l[mid] == n:
            index = mid
        else:
            if n<l[mid]:
                last = mid -1
            else:
                first = mid +1
    return index
    
  
l = [1, 2, 3, 4, 5, 7, 9]
print(Searching(l, int(input())))
