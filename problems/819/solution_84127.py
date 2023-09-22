def filtramultipos(lista,n):
    '''essa funçao recebe uma lista e retorna uma segunda lista com os elementos da lista original que sao multiplos de n
    lista, int -> lista'''
    i=0
    lista2=[]
    
    while i < len(lista):
        if lista[i]% n==0:
            list.insert(lista2, lista2[0], lista[i])
        i=i+1
    return lista2