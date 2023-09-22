def conta_numero(numero,matriz):
    '''Função que, dado um número inteiro e uma matriz de inteiros de tamanho qualquer, retorna quantas vezes o número aparece na matriz.
int,list(list) --> int'''
    linhas = len(matriz)
    colunas = len(matriz[0])
    qtd = 0
    for i in range(linhas):
        qtd = qtd + list.count(matriz[i],numero)
    return qtd