# python3


def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    for i in range(data,0,-1):
        j = i
        while j > 1:
            if data[i-1]<data[j-1]:
                data[i-1], data[j-1] = data[j-1], data[i-1]
                swaps.append([j-1,i-1])
                i = j
            else:
                i=0
    return swaps


def main():   
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    temp=input()
    if 'I'in(temp):
        # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))
    elif 'F'in(temp):
        with open('tests/' + input().replace('\r',''), mode="r") as fails:
            n = int(fails.readline())
            data = list(map(int, fails.readline().split()))

    # input from keyboard
    n = int(input())
    data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
