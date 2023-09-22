def eh_quadrada(m):
    '''Essa funcao recebe uma matrix e retorna se ela é quadrada ou nao
    list->bool'''
    linha = len(m)
    if linha==0:
        return True 
    coluna = len(m[0]) 
    if linha==coluna:
        return True 
    else:
        return False