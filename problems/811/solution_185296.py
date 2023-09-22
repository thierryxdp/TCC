def colchao(medidas,H,L): 
    """Retorna a determinação se é possível(verdade) ou não 
    passar o colchão pela porta, dados as medidas do colchão
    e da porta H e L;
    list, float|int, float|int -> bool"""
    A,B,C = medidas
    if A<H or B<L:
        return False 
    elif H>=A and L>=B : 
        return True