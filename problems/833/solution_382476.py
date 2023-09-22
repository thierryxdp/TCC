def conta_numero(numero, matriz): #Entrada: int e matriz
    contador = 0
    for linha in matriz:
        for coluna in linha:
            if coluna == numero:
                contador += 1
    return contador #Pra cada vez que um número da matriz for igual ao número dado na entrada, o contador soma 1, até ser retornado no final da função. Saída: int