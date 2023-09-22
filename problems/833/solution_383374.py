def conta_numero(numero, matriz):
    '''int + list(list) -> int'''
    qtd = 0
    for i in matriz:
        for j in i:
            if j == numero:
                qtd += 1
            
    return qtd