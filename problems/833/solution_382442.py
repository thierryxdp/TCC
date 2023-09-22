def conta_numero(numero:int, matriz:list) -> int:
    """Função que irá contar quantas vezes um determinado número aparece na matriz e retornará esse valor.

        Parameters:
        numero: valor numérico inteiro que será buscado na matriz
        matriz: lista que representa uma matriz de qualquer tamanho

        Returns:
        valor inteiro que representa o número de vezes que o número apareceu na matriz.

        int, list -> int
    """

    ocorrencia_total = 0
    for i in range(len(matriz)):
        ocorrencia_por_linha = matriz[i].count(numero)
        ocorrencia_total = ocorrencia_total + ocorrencia_por_linha
            
    return ocorrencia_total