def faltante(lista):
    '''Função que verifica qual a peça que esta faltando de uma lista
list -> int'''
    i = 1
    while i < len(lista):
        if  lista[i] - lista[i - 1] > 1: #ent ta faltando uma peça, pq a diferença entre uma peça e a próxima tem q ser um
    i = i+1
    return lista[i]-1