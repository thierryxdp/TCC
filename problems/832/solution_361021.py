def eh_quadrada(x):
    '''
    funcao tem como entrada uma matriz x e retorna se é quadrada ou não
    '''
    if x==[]:
        return True
    p=len(x)
    h=len(x[0])
    if p==h:
        return True
    else:
        return False