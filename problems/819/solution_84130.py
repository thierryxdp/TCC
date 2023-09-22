def filtraMultiplos(lista,n):
    '''essa funçao recebe uma lista e retorna uma segunda lista com os elementos da lista original que sao multiplos de n
    lista, int -> lista'''
    i=0
    lista_mult=[]
    
    while i < len(lista):
        if lista[i]% n==0:
            list.append(lista_mult, lista[i])
            i=i+1
    return lista_mult