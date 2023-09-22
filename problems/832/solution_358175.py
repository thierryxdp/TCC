def eh_quadrada(matriz):
    '''retorna se a matriz fornecida eh quadrada. 
    Uma matriz vazia eh considerada quadrada; list -> bool'''
    linhas=0
    if matriz==[]:
        return True
    for i in matriz[0]:
        linhas=linhas+1
        
	if len(matriz)==linhas:
        return True
    elif len(matriz)!=linhas:
        return False