def colchao (medida, H,L):
    """Retorna um valor booleano indicando se o colcão passa pela porta:
    list, int,int-> bool"""
    a,b,c = medida
    ((H-a)**2 + (L-a)**2)>c