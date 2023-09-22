def peca_perdida(L):
    """
    Descobre qual peça de um jogo está faltando.
    list -> int

    Parameters:
    L: Parâmetro do tipo lista (list);
    
    Returns:
    O número inteiro da peça que faz parte do intervalo [1, N] mas não pertence
    a lista L.
    """

    i = 0
    lista_completa = []
    
    list.sort(L)

    lista_completa = list(range(1, L[-1]+1))

    while i < len(L):
        condicao = L[i] in lista_completa
        if condicao == True:
            list.remove(lista_completa, L[i])  
        i = i + 1

    return (lista_completa[0])