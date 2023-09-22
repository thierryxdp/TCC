def conta_numero(N, matriz):
    """
    	Recebe um <N> e uma <matriz> e retorna quatas vezes <N>
        aparece em <matriz>.
        int, list --> int
    """
    contadorDeAparicao = 0
    for elemento in matriz:
        contadorDeAparicao += list.count(elemento, N)
    return contadorDeAparicao