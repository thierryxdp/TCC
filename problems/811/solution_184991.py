def colchão (a=list,H=int,L=int) -> bool:
    """Função que dada altura H e largura L da porta e A,B,C dimensões de um colchão, da menor pra maior, retorna se será possível passar o colchão pela porta."""
    a = list[A,B,C]
    if (a[2]<=L and a[0]<=H) or (a[1]<=H and a[0]<=L) or (a[0]<=L and a[1]<=H)
        return True
    else:
        return False