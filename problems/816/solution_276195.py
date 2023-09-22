def maiores(lista,n):
    """Dado uma lista contendo números inteiros e um número inteiro n 
    como argumento, retorna uma lista
    com os números maiores que n, exclusive;
    Entrada: Lista contendo inteiros e um número n inteiro
    Saída:lista contendo inteiros"""
    lista_n=lista+[n]
    list.sort(lista_n)
    ind=list.index(lista_n,n)
    lista_n[:ind+1]=[]
    return lista_n