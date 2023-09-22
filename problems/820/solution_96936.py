def posLetra(string,letra,num):
    '''A função indica em qual posição o 2° está no 1° parâmetro,
    caso exista menos ocorrências do que pedido o 3° parâmetro, a 
    função retornará -1
    string, string, float -> float'''
    x = string
    y = letra
    z = num
    i = 0
    quant_contada = 0
    w = str.index(x, y, z)
    
    while len(string) < i:
        if string[i] == letra:
            quant_contada = quant_contada + 1
            i = i + 1
            
    if w <= quant_contada:
        return -1