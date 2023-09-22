def maiores(lista, n):
    '''função que recebe uma lista e um numero n e retorna 
    todos os numeros da lista maiores que n'''
    lista.append(n)
    list.sort(lista)
    posicao=lista.find(n)
    listaFinal=lista[posicao+1:]
    return listafinal