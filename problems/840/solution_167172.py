from math import floor
def bolos (a>2,b>3,c>5):
    '''calculo que determina o máximo de bolos possíveis 
    para se realizar dados os numeros mínimos de ingredientes
    a=farinha, b=ovos e c=leite.'''
    return floor(a/2,b/3,c/5)