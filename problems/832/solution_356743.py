def eh_quadrada(matriz):
    '''Função que recebe uma matriz e retorna se ela é ou nao 
    uma matriz quadrada.
    list(list) -> bool'''
    linha = len(matriz)
    coluna = len(matriz[0])
    for i in matriz:
        if linha == coluna:
            return True
        
        elif lina == [] and coluna==[]:
            return True
        
        else:
            return False