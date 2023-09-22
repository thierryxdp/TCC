def conta_numero(numero,matriz):
    '''
       funaco que dado um numero inteiro e uma 
       matriz de inteiros de tamanho qualquer,
       conta quantas vezes aquele numero aparece 
       na matriz.
       int,int->int
    '''
    quant=0
    for linha in matriz:
        quant=quant+list.count(linha,numero)
    return quant