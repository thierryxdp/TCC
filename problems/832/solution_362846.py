def eh_quadrada(m):
    '''função que recebe uma matriz e verifica se ela é quadrada ou não
    list -> bool'''
    if m==[]:
        return True
    if len(m)==len(m[0]):
        return True
    else:
        return False
    
    #teste 1
    # eh_quadrada(m)