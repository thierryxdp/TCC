def conta_frases(texto):
    '''funcao que diz quantas frases tem em um texto;
str -> int'''
    ponto_final = str.count(texto,'.') - (3*(str.count(texto,'...')))
    ponto_exclamacao = str.count(texto,'!')
    ponto_interrogacao = str.count(texto,'?')
    reticencias = str.count(texto,'...')
    numero_de_frases = ponto_final + ponto_exclamacao + ponto_interrogacao + reticencias
    return numero_de_frases