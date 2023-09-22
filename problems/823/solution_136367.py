def faltante(lista):
    '''retorna o numero faltante na lista dada'''
    '''list -> int'''
    i=0
    
    while i < len(lista):
        if lista[i]!=1:
            return lista[i]
        if lista[i+1]!=2:
            return lista[i+1]
        if lista[i+2]!=3:
            return lista[i+2]
        if lista[i+3]!=4:
            return lista[i+3]
        if lista[i+4]!=5:
            return lista[i+4]
        if lista[i+5]!=6:
            return lista[i+5]
        if lista[i+6]!=7:
            return lista[i+6]
        if lista[i+7]!=8:
            return lista[i+7]