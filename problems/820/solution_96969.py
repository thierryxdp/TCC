def posLetra(string,letra,num):
    '''A função indica em qual posição o 2° está no 1° parâmetro,
    caso exista menos ocorrências do que pedido o 3° parâmetro, a 
    função retornará -1
    string, string, float -> float'''
    x = string
    y = letra
    z = num
    i = 0
    t = 0
    posicao = []
    
    while len(x) > i:
        if string[i] == letra:
            list.append(posicao,i)
        i = i + 1
            
    if len(posicao) >= num:
        return list.pop(posicao, 3)
    else:
        return -1