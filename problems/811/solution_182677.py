def colchao(medidas,H, L):
    '''Recebe uma lista com as medidas de um sofá e a altura e largura da porta da casa e retorna true se o sofá passa pela porta e false se o sofá não passa pela porta; lista, int, int-> boolean'''
    x = medidas[0]
    y = medidas [1]
    z = medidas [2]
    if y >= H and x >= L:
        return False 
    elif y < H and x < L:
        return True 
    elif y > H and x >= L:
        return False
    elif (y > H or y <= H) and x < L:
        return True