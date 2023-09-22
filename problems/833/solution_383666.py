def conta_numero(numero, matriz):
    '''Conta e retorna quantas vezes o número dado aparece 
    na matriz
    int, lista -> inr'''
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[j])):
            if numero == matriz[j]:
                soma += 1
             	
    return soma