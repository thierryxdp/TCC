def conta_numero(numero, matriz):
    '''calcula e retorna quantas vezes um numero aparece em uma matriz.
       int,list --> int'''
    
    qntd = []
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            list.append(qntd,matriz[i][j])
    return list.count(qntd, numero)