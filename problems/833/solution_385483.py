def conta_numero(numero,matriz):
    '''Dado um numero inteiro e uma matriz
    de inteiros de tamanho qualquer, conta
    e retorna quantas vezes aquele numero 
    aparece na matriz
    int, list -> int
    '''
    contador = 0
    for linha in matriz:
        for coluna in linha:
            if coluna == numero:
                contador+=1
 	return contador