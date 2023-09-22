def eh_quadrada(matriz):
    '''
    Recebe uma lista de listas. 
    Se não houver colunas, será quadrada (e vazia);
    Se nº colunas for igual ao nº linhas, será quadrada;
    Se nº colunas diferir do nº linhas, não será quadrada.    
    '''
    if len(matriz) == 0: return True    
    if len(matriz) == len(matriz[0]): return True
    else: return False