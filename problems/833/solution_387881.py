def conta_numero(numero, matriz):
    '''percorre a matriz inteira e verifica se h ́a numero
int, list--> int'''

    total = 0
     
    for i in matriz:
        for j in i:
            if j == numero:
                total += 1

    return total