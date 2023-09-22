def insere(lista,numero):
    '''retorna a lista na posição crescente com o numero inserido
    list,int --> list'''
    lista[0:0] = [numero]
    list.sort(lista)
    return lista