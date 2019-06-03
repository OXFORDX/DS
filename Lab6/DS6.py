from AVL_tree import AVLTree
from RBTREE import RedBlackTree
from random import *

at = AVLTree()
rbt = RedBlackTree()


def count(var):
    for i in range(var):
        at.insert(i)
        rbt.add(i)
    at_count = 0
    rbt_count = 0
    counter = 0
    rbt.prin()
    for i in range(var):
        at_count += at.search(randrange(0, var))
        rbt_count += rbt.find_node(randrange(0, var))[1]
    print(int(at_count / var), int(rbt_count / var))


count(10000)
