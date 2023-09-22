def carros(p,l=5):
    """ calcula o número de carros considerando o número de pessoas e o número de lugares no veículo, caso não seja definido um valor para os lugares l=5; int,int -> int"""
    N=(p//l) + ((p/l)//p%l)
    return N