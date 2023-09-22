def pontos_por_time(gols):
    
    ''' Função que, dadas duas listas informando
        os número de gols em dois jogos de futebol
        entre dois times, retorna um dicionário com
        o número total de pontos de cada time na fase.
        list, list -> dict '''
    
    gols2 = gols.copy()
    gols3 = gols2.copy()
    gols4 = gols3.copy()
    gols5 = gols4.copy()
    
    golspop1 = gols2.pop(0)
    placar1 = golspop1.pop(1)
    golspop2 = gols3.pop(1)
    placar2 = golspop2.pop(1)
    
    golspop3 = gols4.pop(0)
    posicao1 = golspop3[0]
    golspop4 = gols5.pop(0)
    posicao1 = golspop4[0]
    
    ganha1 = placar1[0] > placar1[1]
    ganha2 = placar2[0] > placar2[1]
    empate1 = placar1[0] == placar1[1]
    empate2 = placar2[0] == placar2[1]
 
    cormengo = posicao1 == 'Cormengo'
    flaminthias = posicao1 == 'Flamínthias'
    
    dicionario = {'Cormengo': 0, 'Flamínthias': 0}
    
    
    if cormengo and ganha1 and ganha2:
        dicionario['Cormengo'] = 3+3
    
    if flaminthias and ganha1 and ganha2:
        dicionario['Flamínthias'] = 3+3
        
    if empate1 and empate2:
        dicionario['Cormengo'] = 1+1
        dicionario['Flamínthias'] = 1+1
        
    if cormengo and (empate1 and ganha2) or (empate2 and ganha1):
        dicionario['Cormengo'] = 1+3
        
    if flaminthias and (empate1 and ganha2) or (empate2 and ganha1):
        dicionario['Flamínthias'] = 1+3
        
    
    return dicionario