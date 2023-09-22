def conta_frases(texto):
    '''Função que retorna quantas frases há em um texto, dado o texto a ser
    analisado.
    texto -> string
    return -> int'''
    
    texto = texto.strip()
    
    if texto in ('!', '?', '.', '...'):
        texto = texto.split('!').split('?').split('.')
        
    return len(texto)