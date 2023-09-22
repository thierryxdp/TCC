#retorna True ou False caso um colchão consiga passar, ou não por uma porta de dimensões H e L, dado as mesmas e a lista com dimensões do colchão D.
# medidas,H,L
def Colchao(Medidas,H,L):
    """Funcao que retorna True ou False caso um Colchao consiga passar, ou nao por uma porta de dimensoes H e L, dado mesmas e a lista com dimensoes do colchao D lista(float,float,float) ->int,int"""
    if list (Medidas) [1] <= H:
        return True
    else:
        return False