def colchao(medidas, H, L):
    '''Funcao que dadas as medidas em centimetros de um colcao em lista, a altura e largura de uma porta respectivamente, retornam True, se possivel entrar com esse colchao pela porta, ou False, se nao possivel passar com o colchao pela porta;
    entrada: list, int, int
    saida: bool'''
    
    dim1 = medidas[0]
    dim2 = medidas[1]
    dim3 = medidas[2]

    if (dim1 <= (H or L)) and ((dim2 and dim3) < H or L):
        return True
    else:
            if (dim2 <= (H or L)) and ((dim1 and dim3) < (H or L)):
                return True
            else:
                    if (dim3 <= (H or L)) and ((dim1 and dim2) < (H or L)):
                        return True
                    else:
                        return False