def pi():
	return 3.14

def areacirc(r1):
    return pi()*r1**2
def div(x,y):
    return x/y
def num_bombons(D,vb):
    '''Função que calcula o número possivel de bombons que podem ser comprados dados o dinheiro (D) e o preço de cada bombom (vb) de entrada'''
    return .ceil(div(D,vb))