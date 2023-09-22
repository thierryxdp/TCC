def conta_numero(numero, matriz):
    """Funcao que dado um numero inteiro e uma matriz de inteiros de tamanho qualquer, conta e retorna quantas vezes aquele numero aparece na matriz.
    int, list --> int"""
    qtd_numero = 0
    for linha in matriz:
        for elemento in linha:
            if elemento == numero:
                qtd_numero+=1
                
    return qtd_numero