some = int(input('1, Array, 2, Linkedlist:'))
if some == 1:
    from myarray import Stack

elif some == 2:
    from linked_list import Stack

else:
    print('Restart the program')


def middlestack(n):
    labstack = Stack(n)
    labstack.stackgen(-10, 10, n)
    print('Stack:', end=''), labstack.print()
    summa = 0
    for i in range(n):
        summa += labstack.pop()
    mid = summa / n
    print('Size:', n)
    print('Mid of the stack:', mid)
    print('=' * 10)
    return mid


def call():
    lens = int(input("Enter amount of stacks:"))
    n = int(input("Len of stack:"))
    globalmid = 0
    for i in range(lens):
        mid = middlestack(n)
        globalmid += mid
    print('Middle of all stacks', globalmid / lens)
    return n


n = call()

