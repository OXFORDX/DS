from my_array import myQueue

queue_1 = myQueue()
queue_2 = myQueue()
queue_1.queuegen(20, 2)
print('First plural:'), queue_1.prqueue()
queue_2.queuegen(20, 4)
queue_2.push(3, 2)
print('Second plural:'), queue_2.prqueue()
finalsort = []
for i in range(queue_1.length()):
    element1 = queue_1.pop()
    x = 0
    for j in range(queue_2.length()):
        element2 = queue_2.items[j][0]
        if element1[0] == element2:
            x += 1
    if x == 0:
        queue_2.push(element1[0], element1[1])
print('Merged plural:'), queue_2.prqueue()
for i in range(queue_2.length()):
    finalsort.append(queue_2.pop()[0])
print('Merged plural:', sorted(finalsort))