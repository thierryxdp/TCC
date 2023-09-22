def filtraMultiplos (lista, n):
    '''essa funçao recebe uma lista e retorna uma segunda lista com apenas os elementos da
    lista original que sao multiplos de n
    list, int -> list'''
    i=0
    a=0
    
    while i < len(lista):
        if lista[i]% n == 0:
            a=a + lista[i]
            i=i+1
    return a