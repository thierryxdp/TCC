def insere(lista_numeros,n):
    """Funçao que dada uma lista ordenada(crescente) de números inteiros e 
       um números inteiro n, inclue n na posição correta, ou seja de maneira 
       que a lista permaneça crescente.
       list,int->list
       
       Parâmetros:
       lista_numeros: Lista de números em ordem crescente.
       n: Um n número que deve ser adicionado a lista na posição correta.
       
       Returns: A lista de forma ordenada com o Número n nela.
    """
    lista_numeros.append(n)
    return lista_numeros.sort(lista_numeros)