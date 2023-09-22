def medidas(A,B,C):
    medidas = [A,B,C]
def colchao(medidas,H,L):
    '''Função que retorna true quando o colchão da promoção passa pela porta de João
e retorna False quando o colchão não passa pela porta de João.
    list,int,int-->bool'''
    if medidas[0]<=L and medidas[1]<= H:
        return True 
    else:
        return False