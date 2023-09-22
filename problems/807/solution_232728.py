def conta_frases(frases):
    '''funcao que dada uma frase, conta quantos pontos de interrogacao, exclamacao, tres pontos em sequenciatem no total
    ou um ponto final. 
    str -> int'''
    ponto_final = frases.replace('...','@')
    ponto_exclamacao = ponto_final.replace('!','@')
    ponto_interrogacao = ponto_exclamacao.replace('?','@')
    reticencias = ponto_interrogacao.replace('.','@') 
    return(reticencias.count('@')