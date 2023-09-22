def colchao([A,B,C],H,L):
    """Função que recebe as medidas de um colchão e de uma porta e retorna se é possível a passagem do colchão pela porta;list,int,int->bool"""
    if  L>=A and H>=B:
        return True
    else:
        return False