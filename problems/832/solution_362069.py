def eh_quadrada(matriz):
    '''Recebe uma matriz e retorna se ela eh ou nao uma matriz quadrada; list[list] -> bool'''
    i=0
    nmatriz = []
    if len(matriz)==0:
        return True
    for linha in matriz:
        nmatriz.append(len(linha))
        i+=1
    if (sum(nmatriz)/len(nmatriz))==len(matriz):
        return True
    else:
        return False