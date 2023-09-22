def eh_quadrada(matriz):
    '''retorna se a matriz fornecida eh quadrada. 
    Uma matriz vazia eh considerada quadrada; list -> bool'''
    colunas=0
    for j in matriz:
        colunas=colunas+1
    return colunas