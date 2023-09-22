def conta_numero(numero,matriz):
    """Função que dado um número inteiro e uma matriz, conta e retorna quantas vezes 
       o número aparece na matriz.
       int,list->int"""
    count = 0
    for linha in range(0,len(matriz)):
        for coluna in range(0,len(matriz[linha])):
            if numero in matriz[linha][coluna]:
                count += 1
    return count