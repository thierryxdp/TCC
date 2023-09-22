# retorna True ou False caso um colchão consiga passar, ou não por uma porta de dimensões H e L
# medidas,H,L
def colchao(medidas,H,L):
    '''Funcao que retorna True ou False caso um colchão consiga passar, ou não
        por uma porta de dimensões H e L, dado as mesmas e a lista com dimensões
        do colchão D.
        Entrada: lista(float,float,float) ; Saída: int,int'''
    medidas.sort()
    if medidas[0] > H:
        if medidas[0] > 1:
            return False
        elif medidas[1] > 1:
            return False
        else:
            return True
        elif medidas[1]>H:
            return False
        else:
            return True