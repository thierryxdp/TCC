def maiores(lista,n):
    '''
       Funcao que recebe uma lista de numeros interos
       e um numero inteiro, e retorna outra lista com
       numeros maiores que o numero inteiro de forma ordenada.
       list, int -> list
    '''
    if n in lista:
        list.sort(lista)
        return lista[list.index(lista,n) + 1:]
    else:
        lista.insert(-1,n)
        list.sort(lista)
        return lista[list.index(lista,n) + 1:]
    
def acima_da_media(L):
    '''
       Funcao que recebe uma lista e retorna uma lista ordenada
       list -> list
    '''
    media = int(sum(lista)/len(lista))
    return maiores(lista,media)