def conta_numero (numero, matriz):
    """Função que dado um numero inteiro e uma matriz, conta e retorna quantas vezes aquele numero aparece na matriz;
       int, list -> int."""
    contador = 0
    for lista in matriz:
        for elemento in lista:
            if elemento == numero:
                contador= contador + 1
    return contador