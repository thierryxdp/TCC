def colchao(medidas,H,L):
    '''Recebe uma lista com as medidas de um colchão e retorna True caso ele passe pela porta e False caso não passe;
    list, int, int -> bool'''
    if (medidas[0] < L and medidas[1] < H) or (medidas[0] == L and medidas[1] < H) or (medidas[0] < L and medidas[1] == H):
        return True
    elif (medidas[0] < H and medidas[1] < L) or (medidas[0] == H and medidas[1] < L) or (medidas[0] < H and medidas[1] == L):
        return True
    elif (medidas[2] < H and medidas[0] < L) or (medidas[2] == H and medidas[0] < L) or (medidas[2] < H and medidas[0] == L):
        return True
    elif (medidas[2] < H and medidas[1] < L) or (medidas[2] == H and medidas[1] < L) or (medidas[2] < H and medidas[1] == L):
        return True
    else:
        return False