'''retorna a quantidade de carros necessario, sabendo que um carro transporta 5 pessoas'''
'''p=pessoas; q=quantidade de carros'''
def carros(p):
    q= p // 5
    return (math.ceil(q))