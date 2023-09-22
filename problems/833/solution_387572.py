def conta_numero(numero,matriz):
    '''recebe uma funcao  que dado um numero inteiro e uma matriz de inteiros de
tamanho qualquer, conta e retorna quantas vezes aquele numero aparece na matriz.
int,list->int'''   
    a=0
    
    for i in matriz:
        a+=i.count(numero)
    return  a