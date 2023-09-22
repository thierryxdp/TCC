def bolos(a,b,c):
    '''
Função que calcula e retorna a quantidade máxima de bolos
que João pode fazer dados a quantidade de xícaras de
farinha de trigo(a), ovos (b) e colheres de sopa (c), 
que ele possui em sua casa.
	'''
    qtMinFarinha = a//2
    qtMinOvos = b//3
    qtMinLeite = c//5
    return min(qtMinFarinha, qtMinOvos, qtMinLeite)