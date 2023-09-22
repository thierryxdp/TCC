from math import sqrt

def colchao(medidas,H,L):
    '''funcao que informa se é possivel que um dado colchao, com suas respectivas dimensoes,
    consiga passar por uma porta dadas sua atura e largura. Todas as medidas de entrada estarao em centimetros
    list(int),int,int -> bool'''
    A = medidas[0]
    B = medidas[1]
    C = medidas[2]
    diag_porta = sqrt((L**2)+(H**2))
    if A<L and B<=H:
        return True
    elif A<L and (B*A)< diag_porta:
        return True
    else:
        return False