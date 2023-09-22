def conta_numero(numero,matriz):
    '''
    Função que dado um número inteiro e uma matriz
    de inteiros de tamanho qualquer conta e retorna 
    quantas vezes tal numero aparece na matriz
    '''
    resultado= 0
    for n in matriz:
        resultado = resultado + list.count(n,numero)
    return resultado