def conta_numero(numero,matriz):
    """Essa funcao recebe um Inteiro e uma Matriz.
       Procura-se no interior da matriz quantas ocorrencias
       do Inteiro aparece nas linhas/colunas e retorna
       essa quantidade.
    int, list -> int"""

    contador = 0
    for i in matriz:
        for j in i:
            if numero == j:
                contador += 1
    return contador