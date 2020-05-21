# TO-DO: Complete the selection_sort() function below
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
   newArray = []
   for i in range(len(arr)):
       smallest = findSmallest(arr)
       newArray.append(arr.pop(smallest))
   return newArray 



# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    for k in range(0, len(arr) - 1, 1):
        for i in range(0, len(arr) -1 -k, 1):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp 



    return arr


# STRETCH: implement the Count Sort function below
""" def count_sort(arr, maximum=-1):
    # Your code here
    #Requires us to know the "max" value we'll be sorting
    # The total range of data we'll be sorting sits between 0 and maximum
    if len(arr) == 0:
        return arr
    #if maximum is not given, take max value from input array
    if maximum == -1:
        maximum = max(arr)

    #Make a bunch of buckets
    buckets = [0 for _ in range(maximum)] 

    for x in arr:
        if x < 0:
            return "Error, negative numbers not allowed"
        buckets[x] += 1

        #We have the counts of evrey value in our input array
        #Lets loop through our buckets starting at the samllest index
        j = 0
        for i in range(len(buckets)):
            while buckets[i] > 0:
                arr[j] = i
                j += 1
                buckets[i] -= 1



    return arr

print(count_sort([1,2,3,4])) """

