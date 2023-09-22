def bolos (x,y,z):
    '''
    Funçao que calcula quantos bolos João consegue fazer com determinada quantidade
    de farinha, ovos e leite.
    '''
    return min(x//2, y//3, z//5)