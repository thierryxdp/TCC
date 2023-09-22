def conta_numero(numero,matriz):
    '''Função que recebe um número inteiro e uma matriz de
    números inteiros, que deve, necessariamente, ser informada
    em formato de lista, e retorna quantas vezes o número aparece
    na matriz.
    int,lista -> int'''
    ocorrenciatotal=0
    for i in range(len(matriz)):
        ocorrencianalinha=matriz[i].count(numero)
        ocorrenciatotal=ocorrenciatotal+ocorrencianalinha
    return ocorrenciatotal