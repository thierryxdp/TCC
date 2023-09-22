def conta_frases(texto):
    ''' entrada: 'texto'
        função que recebe um período textual, calcula e retorna
        a quantidade de frases existentes no trecho
        [str-->int]'''
    if '...' in texto:
        texto = texto.replace('...','_')
    if '.' in texto:
        texto = texto.replace('.','_')
    if '?' in texto:
        texto = texto.replace('?','_')
    if '!' in texto:
        texto = texto.replace('!','_')
    if ':' in texto:
        texto = texto.replace(':','_')
    if ';' in texto:
        texto = texto.replace(';','_')
        
    return len(str.split(texto,'_'))