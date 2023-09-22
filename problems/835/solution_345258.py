def melhor_volta(voltas):
    ''' Dada uma matriz contendo os dados do tempo de realizacao das voltas na
    pista de kart de cada corredor, a funcao retorna uma tupla com quem rea-
    lizou a volta mais rapida na pista, qual foi o tempo de realizacao dela e
    em qual volta aconteceu;
    Sao 6 jogadores e cada um deles tem direito a 10 voltas. Eles serao iden-
    tificados pelos seus numeros;
    
    list -> tuple '''
    
    melhoresTempos = []
    melhorVolta = []
    
    
    for jogador in range(6):
        
        melhoresTempos += [min(voltas[jogador])]
        melhorVolta += [list.index(voltas[jogador],min(voltas[jogador]))]
        
    melhorTempo = min(melhoresTempos)
    indiceMelhor = list.index(melhoresTempos,melhorTempo)
        
    return indiceMelhor + 1, melhorTempo, melhorVolta[indiceMelhor]