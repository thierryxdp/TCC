def conta_numero(numero, matriz):
    '''percorre a matriz inteira e verifica se h ́a numero
int, list--> int'''

    total = 0
     
    for item in matriz:
        for item2 in item:
            if item2 == numero:
                total += 1

    return total