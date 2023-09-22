def num_bombons(x,y):
    '''Calcula a quantos bombons é possível comprar a patir da 
    quantia de dinheiro inicial "x",e o preço de cada bombom "y".'''
    return  math.floor(x/y)*x - math.floor(x/y)*y