def conta_numero(numero, matriz):
    """ A função conta_numero, dado um número inteiro e uma matriz de inteiros de tamanho qualquer, conta e retorna quantas vezes aquele número aparece na matriz.
        
        Parameters:
        numero = numero inteiro a ser contado
        matriz = matriz de numeros inteiros a ser analisada

        Testes:
            conta_numero ([[1,1],[2,3]]) == 2
            conta_numero ([]) == 0
            conta_numero ([[1,1,2,3,4,5,6]]) == 2
            conta_numero ([[1],[2],[1],[3],[5],[1]]) == 3

        Returns:
            quantas vezes o número inserido aparece na matriz.
            int, list --> int
    """
    nlin = len(matriz)
    if nlin == 0:
        return 0
    ncol = len(matriz[0])
    contador = 0
    for i in range(nlin):
        for j in range(ncol):
            if numero == matriz[i][j]:
                contador += 1
    return contador