def conta_frases (texto):
    '''Dado um texto, retorne com o número de frases 
       que aparecem nele;
       string -> int '''
    return str.count (texto, '.')+str.count(texto, '!')+str.count (texto, '?') - 2* str.count (texto, '...')