def bolos(A,B,C):
    qntd_farinha = A//2
    qntd_ovos = B//3
    qntd_leite = C//5
    '''Esta função calcula a quantidade total de bolos (completos) feitos com base nas quantidades minimas necessárias de cada um dos itens para a realização do bolo'''
    return min (qntd_farinha,qntd_ovos,qntd_leite)