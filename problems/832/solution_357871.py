def eh_quadrada(matriz):
   	'''Essa função irá retornar verdadeiro caso a metriz seja quadrada ou falso se a matriz não for quadrada
    Entrada: lista | Saída: Boleano 
    '''
    colunas = len(matriz)
    for linhas in matriz :
        if len(linhas) != colunas :
            return False
    
    return True