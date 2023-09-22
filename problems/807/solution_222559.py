def conta_frases(texto):
    '''Retorna a quantidade de frases existentes em um determinado texto. 
    Str -> Int.'''
    texto_copia = texto[:]
    passo1= str.replace(texto_copia, '?', '.')
    passo2 = str.replace(passo1, '!', '.')
    ret = '...'
    if ret in passo2:
        passo3= str.replace(passo2, ret, '.', str.count(passo2, ret))
        passo4 = str.split(passo3, '.')
        return len(passo4) - 1
    else: 
        passo31 = str.split(passo2, '.')
        return len(passo31) - 1