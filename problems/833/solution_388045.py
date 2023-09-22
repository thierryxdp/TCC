def conta_numero(numero,matriz):
    '''Função que dado um número inteiro e uma matriz de inteiros, retorna quantas vezes aquele número aparece na matriz
       int,matriz->int'''
    cont = 0
    for vezes in matriz:
        qtd = list.count(quantidade,numero)
        cont = cont + qtd
    return cont