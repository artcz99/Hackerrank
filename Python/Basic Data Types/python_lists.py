if __name__ == '__main__':

    N = int(input())
    arr = list()

    for j in range(N):
        line = input().split()
        if line[0] == "insert":
            arr.insert(int(line[1]), int(line[2]))
        elif line[0] == "print":
            print(arr)
        elif line[0] == "remove":
            arr.remove(int(line[1]))
        elif line[0] == "append":
            arr.append(int(line[1]))
        elif line[0] == "sort":
            arr.sort()
        elif line[0] == "pop":
            arr.pop()
        else:
            arr.reverse()