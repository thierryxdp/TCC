#Start your python function here
def colisao(a, b):
    x1 = a[0] #Os dois preimeiros itens de a serão a posição e os dois últimos, as dimensões.
    y1 = a[1]
    w1 = a[2]
    h1 = a[3]

    x2 = b[0] #Os dois preimeiros itens de b serão a posição e os dois últimos, as dimensões.
    y2 = b[1]
    w2 = b[2]
    h2 = b[3]

    #Retornamos uma boleana que diz se os objetos se colidem.
    return x1 + w1 > x2 and y1 + h1 > y2 and x2 + w2 > x1 and y2 + h2 > y1