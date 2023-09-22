from collections import Counter


def remove_dups(l1, l2):
    for x in l1:
        l2.append(x)
        if Counter(l1)[x] == 1:
            l1.remove(x)


l1 = [1, 2, 1, 3, 4, 3]
l2 = []


	remove_dups(l1)
	return(l2)