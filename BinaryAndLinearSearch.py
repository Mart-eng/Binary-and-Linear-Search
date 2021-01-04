import time


## I had to write all the print statements because everything kept returning 0 otherwise
#  I also had to increase the list size to see the effect


def main():
    
    print("Linear Search\n")
    numbers = list(range(100000000)) # generate a list of numbers from 0 to 999999
    #print(numbers)

    start = time.time()                 #negligible amount of time
    print("Start time: ",start)
    linear_search(numbers,10)
    end = time.time()
    print("End time: ",end)

    print ("Time it takes for a small range in a list", end - start,'seconds')
    print()

    start = time.time()
    print("Start time: ",start)
    linear_search(numbers,49999999)
    end = time.time()
    print("End time: ",end)
    print ("Time it takes for the middle element in a list", end - start,'seconds')
    print()

    start = time.time()                 #took the longest time out of all of them
    print("Start time: ",start)
    linear_search(numbers,99999999)
    end = time.time()
    print("End time: ",end)
    print ("Time it takes for the last element in a list", end - start,'seconds')







## the binary search was much more efficient over large lists




    

def main2():
    print("Binary Search")
    print()
    
    numbers = list(range(100000000)) # generate a list of numbers from 0 to 999999
    #print(numbers)

    start = time.time()             #negligible amount of time
    print("Start time: ",start)
    binarySearch(numbers,10)
    end = time.time()
    print("End time: ",end)

    print ("Time it takes for a small range in a list", end - start,'seconds')
    print()

    start = time.time()
    print("Start time: ",start)
    binarySearch(numbers,4999999)
    end = time.time()
    print("End time: ",end)

    print ("Time it takes for the middle element in a list", end - start,'seconds')
    print()

    start = time.time()             # took much less time than linear search
    print("Start time: ",start)
    binarySearch(numbers,99999999)
    end = time.time()
    print("End time: ",end)

    print ("Time it takes for the last element in a list", end - start,'seconds')
    







def linear_search(items, target):
    '''finds an item in a list using linear search

        pre: items is a list, target is the value you are looking for
        post: returns the position of the target in the list, -1 if not in list'''
    
    try:
        return items.index(target)
    except ValueError:
        return -1





def binarySearch(items, target):
    '''finds an item in a list using binary search

        pre: items is a list, target is the value you are looking for
        post: returns the position of the target in the list, -1 if not in list'''

    low = 0
    high = len(items) - 1
    while low < high:           #There is a range to search
        mid = (low + high) // 2 #Position of middle item
        item = items[mid]
        if target == item:      #Found it, return the index
            return mid

        elif target < item:     #x is in lower half of range
            high = mid - 1      #cut in half going down

        else:                   #x is in upper half
            low = mid + 1       #cut in half going up

    return -1               #x is not in the list

main()
main2()

