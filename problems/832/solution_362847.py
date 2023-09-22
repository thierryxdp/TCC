def eh_quadrada(m):
    '''função que recebe uma matriz e verifica se ela é quadrada ou não
    list -> bool'''
    if m==[]:
        return True
    if len(m)==len(m[0]):
        return True
    else:
        return False
    
    # testes
    # eh_quadrada([[8,9,8]])
    # saida esperada: False
    # eh_quadrada([[]])
    # saida esperada: True