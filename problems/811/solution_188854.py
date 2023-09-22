def colchao(medidas,H,L):
    """ Função que dadas medidas de um colchão, analisa se é possível atravessar pela porta para a casa
    list,int,int -> bol """
        
    if ((medidas[0]<=H or medidas[0] <= L) and (medidas[1]<=H or medidas[1]<=L)) or  ((medidas[0] <=H or medidas[0] <=L) and (medidas[2]<=H or medidas[2]<=L)):
        return True
    else:
        return False