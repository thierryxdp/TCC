def eh_quaddrada(matriz):
    '''funçao que, fornecida uma matriz, retorna se essa é 
    quarada
    matriz-> bool'''
    a=[]
    if matriz==[]:
    	return True
    if len(matriz)==len(matriz[0]):
        return True
    else:
        return False