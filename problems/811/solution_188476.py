def colchao(medidas,H,L):
    '''dadas as medidas do colchao (em ordem crescente) 
    e a altura H e largura L 
    da porta, podemos saber se o colchao sera capaz de passar
    pela porta sento que ele tem que tdr uma de suas faces 
    paralelas ao chao'''
    x=medidas[0]
    y=medidas[1]
    z=medidas[2]
    if H>=x and L>=y:
        return True
    if H>=y and L>=x:
        return True
    else:
        return False