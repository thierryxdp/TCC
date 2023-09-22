#Questao 1
def eh_quadrada(m):
    '''
    Funcao que dada m(matriz), retorna um booleano que identifica se e uma matriz quadrada. 
    list->bool.
    '''
    if len(m) != 0:
        if len(m) == len(m[0]):
            return True
        else:
            return False      
    else:
        return True