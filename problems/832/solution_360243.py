def eh_quadrada(matriz):
    '''Função que recebe uma matriz e identifica se ela é quadrada ou não.
    entrada da função: list
    saída da função: bool'''
    linha = len(matriz)
    coluna = len(matriz[0])  
    
    if len(matriz) == 0:
        return True
    
   
    return coluna == linha