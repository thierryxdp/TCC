def inverte(frase):
    '''Essa função recebe frase e retorna fraseinvertida 
    e sem pontuações. str-->str'''
    if '-' in frase:
        frase = frase.replace('-',' ')
    if ',' in frase:
        frase = frase.replace(',','')
    if ':' in frase:
        frase = frase.replace(':','')
    if ';' in frase:
        frase = frase.replace(';','')
    if '.' in frase:
        frase = frase.replace('.','')
    if '!' in frase:
        frase = frase.replace('!','')
    if '?' in frase:
        frase = frase.replace('?','')
        
    fraselist = frase.split(' ')
    fat_inv = fraselist[-1:-(len(fraselist)+1):-1]
    inverso = str.join(' ',fat_inv)
    
    return str.lower(inverso)