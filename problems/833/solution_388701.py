def conta_numero(numero,matriz):
    '''funçao que dado um numero inteiro e uma matriz de inteiros de tamanho qualquer, retorna e conta a quantidade de vezes que o numero aparece na matriz; 
    int,list->int'''
    matriz=0
    for linha in matriz:
        matriz= matriz+list.count(linha,numero)
    return matriz