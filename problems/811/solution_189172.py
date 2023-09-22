# retorna True ou False caso um colchão consiga passar, ou não por uma porta de dimensões H e L
# medidas,H,L
def colchao(medidas,H,L):
    '''Funcao que retorna True ou False caso um colchão consiga passar, ou não
        por uma porta de dimensões H e L, dado as mesmas e a lista com dimensões
        do colchão D.
        Entrada: lista(float,float,float) ; Saída: int,int'''
    medidas . sort ()
    if  m [ 0 ] >  h :
        if  m [ 0 ] >  l :
            retornar  False
            elif m[1] > l:
                return False
            else:
                return True
            elif m[1] > h:
                return False
            else:
                return True