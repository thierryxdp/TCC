def pontos_por_time(lista):
    ''' documentação
    list->dict'''
    
    Flaminthians = lista[0][0]
    Cormengo = lista[0][1]
    
    golFlaminthians1 = lista[0][2][0]
    golCormengo1 = lista[0][2][1]
    
    Flaminthians == lista[1][1]
    Cormengo == lista[1][0]
    
    golFlaminthians2 = lista[0][2][1]
    golCormengo2 = lista[1][2][0]
    
    ponto_Cormengo = golCormengo1 + golCormengo2
    ponto_Flaminthians = golFlaminthians1 + golFlaminthians2
    
    return {Flaminthians:ponto_Flaminthians,Cormengo:ponto_Cormengo}

    Flaminthians = lista[0][0]
    Cormengo = lista[0][1]
    
    golFlaminthians1 = lista[0][2][0]
    golCormengo1 = lista[0][2][1]
    
    Flaminthians == lista[1][1]
    Cormengo == lista[1][0]
    
    golFlaminthians2 = lista[1][2][0]
    golCormengo2 = lista[1][2][1]
    pontos_Flaminthians = 0
    pontos_Cormengo = 0
    
    golCormengo = golCormengo1 + golCormengo2
    
    ponto_Flaminthians = golFlaminthians1 + golFlaminthians2
    ponto_Cormengo = golCormengo1 + golCormengo2
    
    return {Cormengo:ponto_Cormengo,Flaminthians:ponto_Flaminthians}