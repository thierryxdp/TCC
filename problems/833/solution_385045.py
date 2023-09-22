def conta_numero(numero: int, matriz: list)-> int:
    """Função que dado um número inteiro e uma matriz de inteiros, retorna quantas vezes
    este número aparece na matriz."""

    n_vezes = 0

    for linha_matriz in matriz:
        for numero in linha_matriz:
            if numero in linha_matriz :
                n_vezes += 1
    
    return n_vezes