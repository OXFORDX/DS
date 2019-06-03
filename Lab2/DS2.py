import time

start_time = time.time()
some = int(input('1, Array, 2, Linkedlist:'))
if some == 1:
    from my_array import myQueue

    print('==' * 2, 'ARRAY', '==' * 2)
    listQueue = []
    numstack = int(input('Enter amount of queue:'))
    lenstack = int(input('Enter len of queue:'))
    amount = ''
    amountlist = []


    def genQueues(i):
        someQueue = myQueue()
        someQueue.queuegen(0, 10, lenstack)
        listQueue.append(someQueue.items)
        x = 0
        if i < 1:
            print('First queue:'), someQueue.print()
            print('==' * 4)
        if i >= 1:
            for k in range(lenstack):
                if listQueue[0][k] == listQueue[i][k]:
                    continue
                else:
                    print(i + 1, ' ', 'This queue is not good:'), someQueue.print()
                    print('==' * 4)
                    return
            amountlist.append(i + 1)
            print(i + 1, ' ', 'This is the same queue:'), someQueue.print()
            print('==' * 4)

        return x


    def call():
        i = 0
        for i in range(numstack):
            genQueues(i)
        return i


    i = call()
    print('Numbers of the same queues:', amountlist)


elif some == 2:
    from mylinked_list import Queue

    print('==' * 2, 'LIST', '==' * 2)
    listQueue = []
    numstack = int(input('Enter amount of queue:'))
    lenstack = int(input('Enter len of queue:'))
    amount = ''
    amountlist = []


    def genQueues(i):
        someQueue = Queue()
        someQueue.queuegen(0, 10, lenstack)
        listQueue.append(someQueue.list)
        x = 0
        if i < 1:
            print('First queue:'), someQueue.prqueue()
            print('==' * 4)
        if i >= 1:
            for k in range(lenstack):
                if listQueue[0][k] == listQueue[i][k]:
                    continue
                else:
                    print(i + 1, ' ', 'This queue is not good:'), someQueue.prqueue()
                    print('==' * 4)
                    return
            amountlist.append(i + 1)
            print(i + 1, ' ', 'This is the same queue:'), someQueue.prqueue()
            print('==' * 4)

        return x


    def call():
        i = 0
        for i in range(numstack):
            genQueues(i)
        return i


    i = call()
    print('Numbers of the same queues:', amountlist)

else:
    print('Restart the program')
print("--- %s seconds ---" % (time.time() - start_time))
