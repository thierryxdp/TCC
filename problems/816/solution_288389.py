def maiores(lista):
    '''funcao que dada uma lista e um numero n retorna outra lista com todos os numeros maiores que n'''
    nova=[]
    lista.append(n)
    lista.sort()
    indice=lista.index(n)
    nova=lista[:indice+1]
    return nova