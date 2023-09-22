def repetidos(l):
    l1 = []
    l2 = l[:]
    contagem = 0
    while contagem < len(l2) - 1:
        if l[0] == l[1]:
            l1.append(l[0])
        	del l[0]
        else:
            del l[0]
        contagem = contagem + 1
    return l1