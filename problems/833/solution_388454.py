def conta_numero(numero, matriz):
    '''Função que recebe um número inteiro e uma matriz 
    de inteiros e retorna quantas vezes esse número aparece
    na matriz.
    assinatura: int, list -> int'''
    contagem = 0
    for linha in matriz:
        for elem in linha:
            if elem == numero:
                contagem += 1
    return contagem