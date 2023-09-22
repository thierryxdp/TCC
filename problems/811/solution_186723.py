def colchao(medidas,H,L):
    ''''''
    [A,B,C] = medidas
    
    if (C<H or C<L or B<H or B<L):
        return True
    else:
        return False