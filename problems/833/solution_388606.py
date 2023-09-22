def conta_numero(numero,matriz):
    '''Função que conta e retorna quantas vezes aquele numero aparece na matriz, 
    dado como entrada um numero inteiro e uma matriz de inteiros de tamanho qualquer ; int,list->int'''
    m=0
    for i in matriz:
        m= m+list.count(i,numero)
    return m