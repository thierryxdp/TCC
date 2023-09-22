def eh_quadrada(matriz):
    '''Função que recebe uma matriz e retorna se ela é ou nao 
    uma matriz quadrada.
    list -> bool'''
    if not matriz:
        return True
    
    linha = len(matriz)
    coluna = len(matriz[0])
    
    for i in matriz:
        if linha == coluna:
            return True
        
        else:
            return False