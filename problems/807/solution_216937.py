def conta_frases(texto):
    '''Retorna o número de frases que aparecem em um texto dado como entrada;
    str -> int'''
    pontofinal = len(str.split(texto,'.'))-len(str.split(texto,'...'))-2
    exclamacao = len(str.split(texto,'!'))-1
    interrogacao = len(str.split(texto,'?'))-1
    reticencias = len(str.split(texto,'...'))-1
    if pontofinal < 0:
        final = pontofinal-pontofinal
    else:
        final = pontofinal
        
    return final+exclamacao+interrogacao+reticencias