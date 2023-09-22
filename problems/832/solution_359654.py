def eh_quadrada(matriz):
    ''' Dado uma matriz, retorna se ela e quadrada ou nao,
    	matriz sem nenhuma linha ou coluna (vazia), e 
        considerada quadrada
        list -> str
     '''
  
    if len(matriz) == len(matriz[0]) or matriz.clear() == matriz:
        return True
    else:
        return False