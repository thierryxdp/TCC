def faltante(L):
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
    lista_completa = (L[-1])
    lista_completa.append(lista_completa[-1]+1)

    while i < len(L[0]):
        condicao = L[0][i] in lista_completa
        if condicao == True:
            list.remove(lista_completa, L[0][i])  
        i = i + 1

    return (lista_completa[0])