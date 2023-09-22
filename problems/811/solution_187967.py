# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas , H , L):
    '''Recebe em uma lista as dimensões AxBxC de um colção e a altura e largura
de uma porta, retornando True ou False, ou seja, se o colchão passa pela porta ou não.
list, int, int --> bool'''
    if H > L:
        if medidas[0] <= L and medidas[1] <= H:
            return True
        else:
            return False
    elif H < L:
        if medidas[0] <= H and medidas[1] <= L:
            return True
        else:
            return False
    else:
        return False

# Casos de teste

# colchao([25,120,220], 200, 100) == True
# colchao([25,205,220], 200, 100) == False
# colchao([25,200,220], 200, 100) == True
# colchao([36,190,209],187,248) == True