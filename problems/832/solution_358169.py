def eh_quadrada(matriz):
    '''retorna se a matriz fornecida eh quadrada. 
    Uma matriz vazia eh considerada quadrada; list -> bool'''
    colunas=1
    for j in matriz:
        colunas=+1
    if len(matriz[0])==colunas:
        return True
    else:
        return False