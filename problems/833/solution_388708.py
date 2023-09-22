def conta_numero(numero,matriz):
    '''funçao que dado um numero inteiro e uma matriz de inteiros de tamanho qualquer, retorna e conta a quantidade de vezes que o numero aparece na matriz; 
int,->int'''
    m=0
    for linha in matriz:
        m= m+list.count(linha,numero)
    return m