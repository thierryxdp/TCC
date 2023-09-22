def colchao(medidas,H,L):
    ''' Função que diz se o colchão passa pela porta ou não.
    		True = Sim,passa
            False = Não,passa
          list,int,int---->bool'''
    A = medidas[0]
    B= medidas[1]
    C= medidas[2]
    if B>H and C>L:
        return False
    else: 
        return True