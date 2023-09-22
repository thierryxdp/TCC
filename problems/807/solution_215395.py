def conta_frases(texto):
    '''Conta o número de frases presentes no texto recebido
    string -> int'''
    frases_ponto = len(str.split(texto,'.'))
    frases_exclamacao = len(str.split(texto,'!'))
    frase_interrogacao = len(str.split(texto,'?'))
    frase_reticencias = len(str.split(str.replace(texto,'...','.'),'.'))
    return frases_ponto + frases_exclamacao + frase_interrogacao  + frase_reticencias