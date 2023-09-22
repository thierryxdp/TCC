def colchao(medidas,H,L):
    '''Dadas as medidas de um colchao, retorna se o mesmo consegue passasr pelas portas de sua casa, de altura H e largura L.
    As medidas do colchao deve ser passadas da menor para a maior.
    list, int, int -> bool'''
    if (H//int(medidas[1]))>1 or (L//int(medidas[2]))>1 or (L//int(medidas[1]))>1 or (H//int(medidas[2]))>1:
        return True
    else:
        return False