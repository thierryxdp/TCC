def colchao(medidas,H,L):
    """Função que recebe as medidas de um colchão e de uma porta e retorna se é possível a passagem do colchão pela porta;list,int,int->bool"""
    if  L>=medidas[0] and H>=medidas[1]:
        return True
    else:
        return False