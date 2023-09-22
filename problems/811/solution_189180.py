#retorna True ou False caso um colchão consiga passar, ou não por uma porta de dimensões H e L
# medidas,H,L
def colchao(medidas,H,L):
    '''Funcao que retorna True ou False caso um colchão consiga passar, ou não
        por uma porta de dimensões H e L, dado as mesmas e a lista com dimensões
        do colchão D'''
    if medidas[1] <= H:
        return True
    else:
        return False