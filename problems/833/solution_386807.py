#Questao 9
def conta_numero(numero,matriz):
    '''
    Funcao que dado um numero inteiro retorna quantas vezes um numero aparece na matriz. 
    int,list->int.
    '''
    repeticoes = 0
    valores = []
    x = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            list.append(valores, matriz[i][j])
    while x < len(valores):
        if numero == valores[x]:
            repeticoes += 1
        x = x + 1
    return repeticoes