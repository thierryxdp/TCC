def repetidos(lista):
    ''' função que recebe como entrada uam lista de números e retorna o número de vezes que um elemento da lista é igual ao elemento anterior;
    list -> list '''
    x = 0
    lista2 = []
    while x < len(lista)-1:
        if lista[x] == lista[x+1]:
            list.append(lista2, True)
        else:
            list.append(lista2, False)
        x = x+1
    return lista2.count(True)