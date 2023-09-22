def conta_numero(numero,matriz):
    '''Função que recebe um número inteiro e uma matriz de inteiros
    e retorna quantas vezes o número aparece na matriz.
    int,list(list)->int'''
    qtd_aparece=0
    for i in matriz:
        for elem in i:
            if elem == numero:
                qtd_aparece=qtd_aparece + 1
    return qtd_aparece