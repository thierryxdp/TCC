def melhor_volta(matrizdostempos):
    '''Informa, a partir de uma matriz em que são contados os tempos de volta
    de 6 corredores, cada um percorrendo 10 voltas, que corredor fez a volta recorde em uma pista de Kart,
    o tempo da sua volta e em que volta 
    entrada: list
    saída: tuple
    '''
    
    # Descobrindo qual foi o menor tempo
    
    temposrecordistas=[]
    for corredor in matrizdostempos:
        list.append(temposrecordistas,min(corredor))
    voltarecorde=min(temposrecordistas)
    
    # Descobrindo qual foi o número da volta de menor tempo
    
    for corredor in matrizdostempos:
        if voltarecorde in corredor:
            numerodavolta=list.index(corredor,voltarecorde)+1
            
            # Descobrindo qual foi o corredor com a volta de menor tempo
            
            corredorrecorde= list.index(matrizdostempos,corredor)+1
            return corredorrecorde, voltarecorde, numerodavolta