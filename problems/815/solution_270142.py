def insere(lista_numero,n):
    """faça uma funçap que dada uma lista ordenada de numeros inteiros e numero inteiro n,
    inclua n na posição correta, ou seja, de tal maneira que a tal lista continue ordenada,
    lista,int-> list
    """
    a=[lista_numero]
    b=[n]
    c=a+b
    c.sort()