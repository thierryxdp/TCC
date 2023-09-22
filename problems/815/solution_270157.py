def insere(lista_numero,n):
    """faça uma funçap que dada uma lista ordenada de numeros inteiros e numero inteiro n,
    inclua n na posição correta, ou seja, de tal maneira que a tal lista continue ordenada,
    lista,int-> lista
    """
    lista = [lista_numero]
    x=list(str(n))
    lista.append(x)
    lista.sort()