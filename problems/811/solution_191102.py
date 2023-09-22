def colchao(medidas, H, L):
    '''dados uma lista com medidas do colchao, ordenadas da menor para a maior.
    E a altura,  H, e largura, L, da porta, retorna se o colchao passa pela porta
    list, int, int -> bool'''
    if (medidas[1]<H or medidas[1]<L) and (medidas[2]<H or medidas[2]<L):
        return 'True'
    return 'False'