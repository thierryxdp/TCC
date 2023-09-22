def eh_quadrada (matriz):
    '''função que dada uma matriz retorna se é ou não
    uma matriz quadrada
    list->bool'''
   
    if len (matriz) == len (matriz[0]):
        return len (matriz) == len (matriz[0])
    else: True