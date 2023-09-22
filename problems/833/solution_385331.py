def conta_numero(numero, matriz):
    '''funcao que dado um numero inteiro
    e uma matriz de tamanho qualquer, retorna
    quantas vezes o mesmo aparece
    entrada: lista, inteiro
    saida: inteiro
    '''
    vezes= 0
    for linha in range(len(matriz)):
        quantidade= list.count(matriz[linha], numero)
        vezes =  vezes + quantidade
    return vezes