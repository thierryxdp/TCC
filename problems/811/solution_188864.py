def colchao(medidas,H,L):
    '''Função que retorna true caso o colchão passe pela porta
    dada as medidas nas entradas, sendo numeros inteiros
    list, int, int-> bool'''
    [A,B,C] = medidas
    if (B<=H) or (B<=L) or (C<=H) or (C<=L):
        return True
    else:
        return False