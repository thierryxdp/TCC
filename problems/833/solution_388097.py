def conta_numero(numero,matriz):
    '''
    funçao que recebe um numero inteiro e uma matriz de 
    inteiros de tamanho qualquer e retorna quantas vezes 
    o numero aparece na matiz
    int,list->int
    '''
    quantidade = 0
    for linha in matriz:
        quantidade = quantidade + list.count(linha,numero)
    return quantidade