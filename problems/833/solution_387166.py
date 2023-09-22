def conta_numero(numero, matriz):
    """A função recebe como entrada um número inteiro e 
    uma matriz (lista) e retorna quantas vezes esse número
    aparece na matriz (outro int)."""
    vezes = 0
    for linha in matriz:
        for elemento in linha:
            if elemento == numero:
                vezes += 1
    return vezes