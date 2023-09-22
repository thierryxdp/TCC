def maiores(lista_numero,n):
    '''Funcao que dada uma lista de numeros inteiros n, retorna outra lista contendo os numeros que sejam maiores que n e ordenados de forma crescente;
    list,int->list'''
    
    lista=insere(lista_numero,n)
    x=((list.index(lista,n))+1)
    
    return lista[x:]