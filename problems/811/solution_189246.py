def colchao(medidas,h,l):
    A=int(A)
    B=int(B)
    C=int(C)
    '''Função que verifica se um colchão passa por uma porta; list,  int, int->Bool'''    
    if(A*B>h*l or A*C>h*l or B*C>h*l):
        return'False'
    elif(A*B<h*l or A*C<h*l or B*C<h*l):
        return 'True'