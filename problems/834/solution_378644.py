def media_matriz(matriz):
    '''calcula a media dos elementos de uma matriz nao nula com duas
       casas decimais
       list -> float'''
    
    soma=0
    elementos=0
    
    for i in matriz:
        for j in i:
            soma+=j
            elementos+=1
    return round(soma/elementos, 2)