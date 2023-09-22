def colchao(medidas,H,L):
    """ Recebe as medidas crescentes (a,b,c , como elementos da lista )de um colchão e retorna se é possível que ele passe pela porta de dimensões H,L. Lista, Float--> Bool."""
    
    a = medidas[0]
    b= medidas [1]
    c= medidas[2]
    if c<= H and c<= L:
        return True
    elif b <=H  or b <= L:
        return True
    else:
        return False