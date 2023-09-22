def conta_numero(numero: int, matriz: list) -> int:
    """Conta quantas vezes um número inteiro qualquer aparece em uma matriz de
       números inteiros qualquer

       Parameters:
       numero: Número inteiro de referência para a contagem
       matriz: Lista de lista a ser analisada, na qual cada lista representa uma
       linha e cada lista de lista representa uma coluna

       Return:
       Dados os parâmetros "numero" e "matriz", retorna quantas vezes o
       parâmetro "numero" aparece no parâmetro "matriz"

       Examples:
       conta_numero(1, [[1, 2], [2, 2]]) == 1
       conta_numero(2, [[1, 2], [2, 2]]) == 3
       conta_numero(0, [[0, 0], [0, 0], [0, 0]]) == 6
    """

    resultado = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                resultado = resultado + 1

    return resultado