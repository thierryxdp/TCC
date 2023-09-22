def passarnaporta(A,B,C,H,L):
    '''Função que retorna true caso o colchão passe pela porta
    dada as medidas de entrada, sendo numeros inteiros
    list -> bool'''
    if C<H or C<L or B<H or B<L:
        return True
    else:
        return False