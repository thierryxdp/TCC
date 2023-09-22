def colchao(medidas,H, L):
    '''Recebe uma lista com as medidas de um sofá e a altura e largura da porta da casa e retorna true se o sofá passa pela porta e false se o sofá não passa pela porta; lista, int, int-> boolean'''
    x = medidas[0]
    y = medidas [1]
    z = medidas [2]
    if y >= H and x >= L and z >=L:
        return True
    elif x < H and x < L and y > H and y > L and z > L and z > H:
        return False