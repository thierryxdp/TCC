def media_matriz(m):
    divisor = len(m) * len(m[0])
    cont = 0
    
    for linha in range(len(m)):
        for indice in range(len(m[linha])):
            cont = cont + m[linha][indice]
            
    div = cont/divisor
    fim = round(div, 2)
    return fim