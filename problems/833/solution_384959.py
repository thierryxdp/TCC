#Questão 2
def conta_numero(numero, matriz):
    """Função que retorna quantas vezes um dado número 'num'
    aparece na matriz;
    int, list -> int"""
    vezes = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if numero == matriz[i][j]:
                vezes += 1
    return vezes