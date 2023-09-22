def colchao (medida, H,L):
    """Retorna um valor booleano indicando se o colcão passa pela porta:
    list, int,int-> bool"""
    return (H**2 + L**2)**(1/2) > medida[0] or medida[1] or medida [2]