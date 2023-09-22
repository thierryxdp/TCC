def faltante(peças):
    '''Essa função descobre qual das peças está faltando '''
    
    TOTAL = len(peças) + 1
    COMPLETO = list(range(TOTAL+1))
    indice = 0
    list.remove(COMPLETO,0)
    
    while TOTAL > indice:
        if COMPLETO(indice) in peças:
            indice += 1
          
        else:
            return COMPLETO(indice)