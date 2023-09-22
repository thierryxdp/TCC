def posLetra(x,y,z):
    '''Esta função recebe uma string, letra e numero
    assim demonstra o local onde a letra ocorre
    assinatura str, str, int -> int'''
    if x.count(y) < z :
        return -1
    if x.count(y) > = z :
        return x.find(y)