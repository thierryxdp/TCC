def eh_quadrada(matriz):
    '''Função que identifica se uma matriz é quadrada. 
    list->bool'''
    
    n_linha=len(matriz)
    ret=[]
           
    for i in range(n_linha):
        for j in range(len(matriz[0])):
            if n_linha!= len(matriz[0]):
                return False
            if n_linha == []:
                return True
            
    return True