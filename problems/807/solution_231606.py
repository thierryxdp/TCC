def conta_frases(texto):
    '''função que conta o número de frases que aparecem em um texto,
    considerando que as frases terminam com ponto final, exclamação,
    interrogação ou reticências sem serem usados em sequência
    str->int'''
    
    ponto_final = frases.replace("...", '@')
    ponto_exclamacao = ponto_final.replace("!", '@')
    ponto_interrogacao = ponto_exclamacao.replace("?", '@')
    reticencias = ponto_interrogacao.replace(".", '@')
    return reticencias.count('@')