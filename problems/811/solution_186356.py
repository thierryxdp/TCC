#medida a b c
#dois lados tem q ser pelo menos menor que pelo menos uma das medidas das portas
#se tem muitos pelo menos, melhro fazer com not
#ou seja
#se dois dos lados não for menor que uma medida da porta, false
def colchao(medidas, H, L):
    """ medidas são a largura do colchao, H e L sao a largura da porta.int->str."""
    A = medidas[0]
    B = medidas[1]
    C = medidas[2]
    if ((A and B)or (A and C) or (B and C) > H and L):
        return False
    else:
        return(True)