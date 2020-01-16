def printReverse(string):
    helper(0, string)


def helper(index, string):
    if not string or index >= len(string):
        return
    helper(index + 1, string)
    print(string[index])


string = input("Enter string to printed in reverse order: ")
printReverse(string)
