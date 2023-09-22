def repetidos(l):
    l1 = []
    contagem = 0
    while contagem < len(l):
        if l[0] == l[1]:
            l1.append(1)
        	del l[0]
        else:
            del l[0]
        contagem = contagem + 1
    return l