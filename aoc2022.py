def createList(filename):
    list = []
    f = open(filename, "r")
    for x in f:
        if x == "\n":
            list.append(0)
        else:
            list.append(int(x))

    return list

def findLargest(list):
    largest = list[0]

    for x in list:
        if x > largest:
            largest = x

    print(f"Largest is {largest}")

    return largest

def findLargestN(list, n):
    list.sort()
    newList = []
    sum = 0
    for x in range(n):
        next = list.pop()
        newList.append(next)
        sum = sum + next
    print(f"Largest {n} are {newList}")
    print(f"The sum of the largest {n} is {sum}")


    return sum

def main():

    mylist = createList('d1.txt')
    #mylist = (1000, 2000, 3000, 0, 4000, 0, 5000, 6000, 0, 7000, 8000, 9000, 0,10000)
    clist = []
    sum = 0
    for x in mylist:
        if x == 0:
            clist.append(sum)
            sum = 0
        else:
            sum = sum + x
    
    print(clist)
    
    l = findLargest(clist)


    l3 = findLargestN(clist, 3)


if __name__ == "__main__":
    main()