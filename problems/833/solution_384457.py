def conta_numero(numero,matriz):
    '''
    Função que dado um numero inteiro e uma matriz de inteiros de tamanho qualquer,
    conta e retorna quantas vezes aquele numero aparece na matriz;
    int,list(list) -> int
    '''

    qtd = 0

    for linha in matriz:
        for elemento in linha:
            if elemento == numero:
                qtd = qtd + 1
    return qtd