def filtra_pares(tup):
    '''recebe uma tupla de quatro elementos inteiros e 
    retorna uma nova tupla apenas com os elementos pares
    tuple->tuple'''
    if par(tup[0])==0:
        tupFinal=tup[0]
    if par(tup[1])==0:
         tupFinal=tupFinal+tup[1]
    if par(tup[2])==0:
        tupFinal=tupFinal+tup[2]
    if par(tup[3])==0:  
        tupFinal=tupFinal+tup[3]
    return tupFinal
    
def par(x):
    '''retorna zero se o elemento x for par e um se for impar
    int->int'''
    if (x%2)==0:
        return 0
    else:
        return 1