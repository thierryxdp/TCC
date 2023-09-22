def maiores(lista,n):
    ''' funcao que dado uma lista de entrada retorna outra lista que adiciona somente os numeros maiores que n
        list[int,int,int] --> list[int,int] '''
    list.append(lista,n)
    list.sort(lista)
    numero = list.index(lista,n)
    del lista[:numero+1]
    
    return lista