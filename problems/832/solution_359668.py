def eh_quadrada(matriz):
    ''' Dado uma matriz, retorna se ela e quadrada ou nao,
    	matriz sem nenhuma linha ou coluna (vazia), e 
        considerada quadrada
        list -> str
     '''
    matriz_aux = []
    matriz.append(matriz_aux)
    if len(matriz)+1 == len(matriz[0]):
        return True
    else:
        return False