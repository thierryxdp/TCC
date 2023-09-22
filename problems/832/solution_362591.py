def eh_quadrada(ls):
    """Essa função serve para identificar se uma matriz (ls) é quadrada.
    list->bool"""
    if ls == []:
        return True
    if len(ls[0]) == len(ls):
        return True
    else:
        return False

#eh_quadrada([[1,2,3],[4,5,6],[7,8,9]]) == True
#eh_quadrada([[1,2],[4,5],[7,8]]) == False
#eh_quadrada([]) == True