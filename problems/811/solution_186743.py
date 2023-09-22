def colchao(medidas,H,L):
    ''' Função que dada uma medida, altura e largura, ela retorna se a altura e largura cabe na
    medida, se sim, ela retorna verdadeiro, caso não, retorna falso
    List -> bool, bool'''
    [A,B,C] = medidas
    
    if (C<H or C<L or B<=H or B<L):
        return True
    else:
        return False