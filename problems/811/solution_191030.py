def colchao(medidas,h,l):
    '''Função que determina se um colchao com medidas a,b,c 
    passa por uma porta com altura h e largura l.
    obs: a lista das medidas do colchao é em ordem crescente.
    valores: list, int, int ---> bool'''
    if medidas[0] <= max(h,l) and medidas[1] <= max(h,l):
        return True
    else:
        return False