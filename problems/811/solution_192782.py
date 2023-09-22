def colchao(medidas, H, L):
    '''Funcao que dadas as medidas em centimetros de um colcao em lista, a altura e largura de uma porta respectivamente, retornam True, se possivel entrar com esse colchao pela porta, ou False, se nao possivel passar com o colchao pela porta;
    entrada: list, int, int
    saida: bool'''
    
    dim1 = medidas[0]
    dim2 = medidas[1]
    dim3 = medidas[2]

    if (dim1 <= H) and ((dim2 or dim3) < L):
        return True
    if (dim1 <= L) and ((dim2 or dim3) < H):
        return True
    else:
        if (dim2 <= H) and ((dim1 or dim3) < L):
            return True
        if (dim2 <= L) and ((dim1 or dim3) < H):
            return True
        else:
            if (dim3 <= H) and ((dim1 or dim2) < L):
                    return True
            if (dim3 <= L) and ((dim1 or dim2) < H):
                    return True
            else:
                        return False