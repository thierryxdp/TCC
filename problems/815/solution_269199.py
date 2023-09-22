def insere(lista_numeros, n):
    """Função que dada uma lista ordenada de números inteiros e um número inteiro n, inclui n na lista de modo que ela continue crescente.
    (int, int) -> int """
    
    número = str(n)
    lista_criada = lista_numeros + list(número)

    lista_criada[-1] = int(lista_criada[-1])
    list.sort(lista_criada) 

    return lista_criada