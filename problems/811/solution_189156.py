def colchao(lista,H,L):
    """Função que a partir das medidas do colchao, vai retornar se passa ou não passa na porta de João"""
    
    [A,B,C]=lista
    
    if (C<H or C<L or B<=h or B=L):
        return True
    else:
        return False