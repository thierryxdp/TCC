def conta_numero(numero,matriz):
    '''Função que receba como entrada uma matriz de inteiros 	
    	de tamanho qualquer e um número inteiro e retorne
        quantas vezes o número aparece na matriz.
        list, int --> int'''
    contagem = 0
    linha = 0
    for linha in matriz:
        contagem = linha.count(numero)
    return contagem