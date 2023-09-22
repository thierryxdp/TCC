def eh_quadrada(matriz):
    '''recebe uma matriz e retorna um valor booleano dizendo se a matriz é ou não é quadrada;list->boolean'''
    linha=len(matriz)
    listacoluna=[]
    if len(matriz[0])==0 and len(matriz)==1:
        return True
    else:
        for m in range(len(matriz)):
        	for n in range(len(matriz[0])):
        		listacoluna.append(n)
        	coluna=max(listacoluna)+1  
            if coluna==linha:
                return True
            else:
                return False