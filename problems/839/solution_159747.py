import.math
def carros(passag,assent=5):
    '''dado o número de passageiros, retorna a quantidade de carros com 5 lugares. 
    Para carros não convencionais, definir a capacidade deste em 'assent'''
    return math.ceil(passag/assent)