def conta_frases(texto):
    '''Retorna o número de frases que aparecem em um texto dado como entrada;
    str -> int'''
    final = len(str.split(texto,'. '))-1
    exclamacao = len(str.split(texto,'!'))-1
    interrogacao = len(str.split(texto,'?'))-1
    reticencias = len(str.split(texto,'...'))-1
    num_frases = final+exclamacao+interrogacao+reticencias
    return num_frases