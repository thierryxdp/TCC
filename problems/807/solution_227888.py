def conta_frases(texto):
    '''Função que conta quantas frases existem num texto
    com base na pontuação usada(ponto final, exclamação, interrogação
    etc.)
    valores: str --> int'''
    reticencias='...'
    #Como reticencias usa 3 pontos, se fizer a contagem apenas de pontos
    #gera um conflito
    return (texto.count('.')-texto.count(reticencias)*3)+ texto.count('!')+ texto.count('?')+ texto.count(reticencias)