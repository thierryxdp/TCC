def meida_matriz(matriz):
    '''retorna a media de todos os numeros da matriz com 2 casas decimais
    list->float'''
    
    soma=0
    quantidade=0
    
    for l in range(len(matriz)):
        for c range(len(matriz[l])):
            soma+=c
            quantidade+=1
   
    return round((soma/quantidade),2)