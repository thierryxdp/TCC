def insere(lista_numero, n):
    """Retorna, dados uma lista ordenada de numeros inteiros e um numero inteiro n, n na posição correta, deixando apenas uma lista com numeros maiores que n 
       Entrada: list, int;
       Saida: list;
    """
    lista_numero.append(n)
    lista_numero.sort()
    y= list.index(lista_numero,n)
    b= lista_numero[y:]
    return b