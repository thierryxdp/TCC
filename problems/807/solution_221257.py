def conta_frases(texto):
    '''Função que calcula o número de frases de um texto
    str -> int'''
    if '...' in texto:
        numero_reticencias = str.count(texto, '...')
        numero_interrogacao = str.count(texto, '?')
        numero_exclamacao = str.count(texto, '!')
        numero_ponto_final = str.count(texto, '.') - 3*numero_reticencias
        numero_frases = numero_reticencias + numero_interrogacao + numero_exclamacao + numero_ponto_final
        return numero_frases
    else:
        numero_interrogacao = str.count(texto, '?')
        numero_exclamacao = str.count(texto, '!')
        numero_ponto_final = str.count(texto, '.')
        numero_frases = numero_interrogacao + numero_exclamacao + numero_ponto_final
        return numero_frases