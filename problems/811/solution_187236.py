def colchao(medidas,H,L):
    '''funcao que informa se é possivel que um dado colchao, com suas respectivas dimensoes,
    consiga passar por uma porta dadas sua atura e largura. Todas as medidas de entrada estarao em centimetros
    list(int),int,int -> bool'''
    A = medidas[1]
    B = medidas[2]
    C = medidas[3]
    if A<=(L) and B>=H:
        return True
    else:
        return False