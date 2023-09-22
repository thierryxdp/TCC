def conta_frases(frases):
    '''
    funcao que dada uma frase e contabiliza  as pontuações( pontos de exclamação,interrogação
    , tres pontos em sequencia (reticencias) e ponto final.pontos de exclamaçao ou de interrogaçao nao
    aparecerao repetidos em sequencia no texto e esses simbolos so
    aparecem no texto terminando uma frase. frases--->str, return--->int'''
 
    
    ponto_final = frases.replace("...", '@')
    ponto_exclamacao = ponto_final.replace("!", '@')
    ponto_interrogacao = ponto_exclamacao.replace("?", '@')
    reticencias = ponto_interrogacao.replace(".", '@')
    
    
    return reticencias.count('@')