def conta_frases(texto):
    '''Retorna a quantidade de frases dado um texto como parâmetro; string -> int'''
    texto_so_ponto_final = texto.replace('!','.').replace('?','.').replace('...','.')
    return len(texto_so_ponto_final.strip('.').split('.'))