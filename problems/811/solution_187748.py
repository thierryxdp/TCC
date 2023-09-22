def conchao(medidas,H,L):
    """Função que recebe as medidas AxBxC de um colchão,
    a altura(H) e a largura(L) de uma porta. A função 
    retorna se o colchão passa ou não pela porta.
    list,int,int->bool
    """
    if H>=A and L>=B or H>=B and L>=A or H>=C and L>=B or H>=B and L>=C or  H>=A and L>=C or H>=A and L>=C:
        return True
    else:
        return False