def faltante(lis):
    '''
    retorna qual numero inteiro do intervalo esta em falta
    list -> int
    '''
    somapa=0
    i=0
    while i<(len(list)+1):
        somapa=somapa+(i+1)
        i=i+1
    return somapa-sum(lis)