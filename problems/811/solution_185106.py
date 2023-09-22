def colchao(medidas,H,L):
    '''dada uma lista contendo as dimensões A,B e C de um colchão em centimetros
    (da menor para a maior) e dois inteiros H e L, que simbolizam, respectivamente,
    a altura e a largura de uma porta em centimentros, retorna True se o colchão
    passa pela porta, e False caso não passe;
    list, int, int --> bool'''
    A = medidas[0]
    B = medidas[1]
    C = medidas[2]
    
    if H < C and L < C and H < B and L < B:
        return False
    else:
        return True