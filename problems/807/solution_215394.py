def conta_frases(texto):
    '''Conta o número de frases presentes no texto recebido
    string -> int'''
    frases_ponto = len(str.split(texto,'.'))-1
    frases_exclamacao = len(str.split(texto,'!'))-1
    frase_interrogacao = len(str.split(texto,'?'))-1
    frase_reticencias = len(str.split(str.replace(texto,'...','.'),'.'))-1
    return frases_ponto + frases_exclamacao + frase_interrogacao  + frase_reticencias