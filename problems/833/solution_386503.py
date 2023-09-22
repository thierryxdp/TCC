conta_numero(numero,matriz):
    'dado um numero inteiro e uma matriz, conta a quantidade de vezes que o numero aparece int, list-> int' 
    contagem = 0
    for j in range (len(matriz)):
        for i in range (len(matriz[0])):
            if numero = matriz[j][i]:
                contagem = contagem + 1
    return contagem