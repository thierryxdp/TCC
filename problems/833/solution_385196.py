def conta_numero(numero,matriz):
    ''' Função que dados um número inteiro e uma matriz 
    de inteiros de tamanho qualquer, retorna a quantidade
    de vezes que o número aparece na matriz.
    Entrada: int,list
    Retorno: int '''
    
    nvezes = 0
    for i in range(matriz):
        nvezes = nvezes + list.count(i,numero)
    return nvezes