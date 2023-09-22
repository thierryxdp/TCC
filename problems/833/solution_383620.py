def conta_numero (numero, matriz):
    """Função que, dado um número e uma matriz, retorna quantas vezes o número aparece na matriz.
    Entrada: int e lista.
    Saída: int."""
    
    contador = 0
    for linha in matriz:
        for coluna in linha:
            if coluna == numero:
                contador = contador + 1
    return contador