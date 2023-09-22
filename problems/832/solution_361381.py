ef eh_quadrada(matriz):
    '''Função que dada uma matriz retorna se o seu número de colunas é igual ao número de linhas
    entrada:list
    saida:bool'''
    if len(matriz)==0:
        return True
    elif len(matriz)==len(matriz[0]):
        return True
    else:
        return False