def colchao(medidas, H, L):
    '''dadas as medidas do colchao em forma de lista e as dimensoes da porta, a funcao retorna se sera possivel ou nao passar o colchao
    list, int, int -> bool'''
    menor = medidas[0] # A
    medio = medidas[1] # B
    maior = medidas[2] # C
    if menor <= H and medio <= L:
        return True
    elif medio <= H and menor <= L:
        return True
    else:
        return False