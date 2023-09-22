def colchao(colchao, H, L):
    """
    Avalia se é possível passar um colchão, com determinadas dimensões, por
    certa porta.
    list, int, int -> bool.

    Parameters:
    colchao: Parâmetro das dimensões do colchão, do tipo tista (list);
    H: Parâmetro numérico H (altura do colchão), do tipo inteiro (int);
    L: Parâmetro numérico L (largura do colchão), do tipo inteiro (int).
    
    Returns:
    A quantidade de palavras em uma frase.
    """

    list.sort(colchao)
    
    A = colchao[0]
    B = colchao[1]
    C = colchao[2]

    
    dimensoes_porta = (H * L)


    if (A <= L and B <= H):
        return True
    else:
        return False