def maiores(lista_int,n):
    
    """
    lista,int--->lista
    Foi transformado o valor n em uma lista para que a concatenacao fosse
    possivel.Em seguida a lista dada na entrada foi concatenada com a lista
    do valor n e, após o comando sort(ordem crescente da lista unida), se
    fez uma nova lista indo do valor x+1(para nao incluir o x na lista)
    até o fim
    """
    
    lista0=[n]
    
    lista=lista_int+lista0
    list.sort(lista)
    
    x=list.index(lista,n)
    
    return lista[x+1:]