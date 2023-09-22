# Ira retornar True ou False caso o colchao passar ou nao pelas determinadas dimensoes 
# medidas,H,L
def colchao(medida,H,L):
    """Funçao que retorna True ou False caso o colchao consiga passar,ou nao por uma porta de dimensoes H e L dado as mesmas e a lista com dimensões do colchão lista(float,float,float)->int,int""" 
    if list (medidas)[1] <= H:
        return True
    else:
        return False