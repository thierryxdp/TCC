def media_matriz(m):
    ''' Esta função calcula a média de todos os elementos de
    uma matriz e retorna o resultado com duas casas de precisão
    list -> float'''
    cont = 0
    i = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            cont += m[i][j]
   	
    num = len(m[i]) * len(m)
    
    div = cont/num
    
    return round(div,2)