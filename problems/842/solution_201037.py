def pontos_por_time(jogo):
    '''
    '''
    pontos= {}
    cormengo = 0
    flaminthians = 0 
    
    cormengo = jogo[0][2][0]
    flaminthians = jogo[0][2][1]
    
    if flaminthians > cormengo:
        pontos['flaminthians']=3
    elif cormengo > flaminthians:
        pontos['cormengo']=3
    else:
        pontos['flaminthians']=2
        pontos['cormengo']=2
        
    cormengo= jogo[1][2][1]
    flaminthians= jogo[1][2][0]
    
    if flaminthians > cormengo:
        pontos['flaminthians']+=3
    elif cormengo > flaminthians:
        pontos['cormengo']+=3
    else:
        pontos['flaminthians']+=2
        pontos['cormengo']+=2
        
    return pontos, list(dict.keys(jogo)