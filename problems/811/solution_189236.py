def colchao(medidas,h,l):
    '''Parâmentros de entrada:
    medidas: lista com dimensões A,B,C do colchão em formato int;
    h:int
    l:int
    Retorno:Booleano'''
if(A*B>h*l or A*C>h*l or B*C>h*l):
    return False
else:
    return True