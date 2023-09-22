'''retorna a quantidade de carros necessario, sabendo que um carro transporta 5 pessoas'''
'''p=pessoas; q=capacidade do carros'''
import math
def carros(p,q=5):
    n=p/q
    return(math.ceil(n))