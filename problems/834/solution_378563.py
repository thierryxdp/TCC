def media_matriz(m):
    cont = 0
    
    for linha in range(len(m)):
        for indice in range(len(m[linha])):
            cont = cont + m[linha][indice]
            
    div = cont/len(m) * len(m[0])
    fim = round(div, 2)
    return fim