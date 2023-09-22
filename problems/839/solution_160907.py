from math import ceil 
def carros(x,y=5):
    '''calcula e retorna a quantidade de carros necessaria pra transportar um numero x de pessoas'''
    return ceil(x//y)