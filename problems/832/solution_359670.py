def eh_quadrada(matriz):
    ''' Dado uma matriz, retorna se ela e quadrada ou nao,
    	matriz sem nenhuma linha ou coluna (vazia), e 
        considerada quadrada
        list -> bool
     '''
    matriz_aux = []
    matriz.append(matriz_aux)
    if len(matriz) == len(matriz[0])+1 or len(matriz) == 0:
        return True
    else:
        return False