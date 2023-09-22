def colchao(medidas,H,L):
    '''Dado as medidas de um colchao e a altura e largura de uma porta retornará
    "True" caso o colchão passe e "False" caso ele não passe pela porta.
    (lista,int,int => bool).'''

    if medidas[1] > H:
        return False

    else:
    #medida[1] <= H
        return True