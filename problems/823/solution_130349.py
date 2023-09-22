def faltante(pecas):
    '''Essa função descobre qual das peças está faltando;
    list->int'''
    
    TOTAL = len(pecas) + 1
    COMPLETO = list(range(TOTAL+1))
    indice = 0
    list.remove(COMPLETO,0)
    
    while TOTAL > indice:
        if COMPLETO[indice] in pecas:
            indice += 1
          
        else:
            return COMPLETO(indice)