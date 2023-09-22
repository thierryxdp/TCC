def colchao(medidas,h,l):
    '''Função que verifica se um colchão passa por uma porta; list,  int, int->Bool'''
    medidas=[A,B,C]
    if(A*B>h*l or A*C>h*l or B*C>h*l):
        return'False'
    elif(A*B<h*l or A*C<h*l or B*C<h*l):
        return 'True'