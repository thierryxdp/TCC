'''retorna a quantidade de carros necessario, sabendo que um carro transporta 5 pessoas'''
'''p=pessoas; q=quantidade de carros'''
def carros(p,q=5):
    n = p // q
    return (n + 1)//1