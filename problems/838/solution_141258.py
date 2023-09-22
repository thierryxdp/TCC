def num_bombons(dinheiro, preco):
    '''Calcula quantos bombons e troco
    float,float->int'''
    return int(dinheiro / preco), dinheiro % preco
    
def falta(dinheiro, preco):
    '''Calcula quanto falta para mais um bombom
    float,float->float'''
    n, troco = bombons(dinheiro, preco)
    return preco - troco