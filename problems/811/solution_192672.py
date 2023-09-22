def colchao(medidas,H,L):
    """função que calcula e retorna se um colchão dado as sua medidas passa por uma porta de altura H e largura L; list,int->bool"""
    return (medidas[1]*medidas[2]<=H*L)or(medidas[1]<=H)