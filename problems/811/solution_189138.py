def colchao(medidas,H,L):
    """funçao que dadas as medidas de um colchao e de uma porta 
    retorna se é possivel passar com o colchao na porta; list,int,int->bool"""
    if medidas[0]<L and medidas[1]<H:
        return True
    else:
        return False