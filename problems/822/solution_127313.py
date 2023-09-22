def repetidos(lista):
    '''Recebe como entrada uma lista de números
    e retorna o número de vezes que um elemento
    da lista é igual ao elemento anterior.
    list -> int'''
    x = 0
    rep = []
    while x < len(lista):
        if lista.count(lista[x]) > 1:
            
            rep += [lista[x]]
        return rep