def conta_numero(numero, matriz):
    '''percorre a matriz inteira e verifica se há número
    int, list--> int'''

    total = 0  #inicia total em zero

    for item in matriz:  #para cada item da matriz:
        for item2 in item:  #para cada item de cada item:
            if item2 == numero:  #se o item do item for igual ao número:
                total += 1  #incrementa total
    
    return total  #retorna total