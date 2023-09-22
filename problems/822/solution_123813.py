def repetidos(l):
    '''funcao que receba como entrada uma lista de numeros, e retorne o numero de vezes que um elemento da lista e igual ao elemento anterior;
    list->list''' 
    x = 0
    l_1 = []
    while x < len(l)-1:
        if l[x] == l[x+1]:
            list.append(l_1, True)
            else:
                list.append(l_1, False)
                x += 1
                return l_1.count(True)