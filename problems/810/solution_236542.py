def inverte(texto):
    'Dada uma frase, retorna o inverso da frase sem pontuação e sem letras maiúsculas. Entrada: str. Saída: str.'
    if '...' in texto:
        texto=str.replace(texto, '...',' ')
    if '.' in texto:
        texto=str.replace(texto, '.',' ')
    if '?' in texto:
        texto=str.replace(texto, '?',' ')
    if '!' in texto:
        texto=str.replace(texto, '!',' ')
    if ',' in texto:
        texto=str.replace(texto, ',',' ')
    if ';' in texto:
        texto=str.replace(texto, ';',' ')
    if ':' in texto:
        texto=str.replace(texto, ':',' ')
    if '-' in texto:
        texto=str.replace(texto, '-',' ')
    texto=str.lower(texto)
    separa_e_inverte=(str.split(texto))[-1::-1]
    texto_invertido=(' ',separa_e_inverte)
    return texto_invertido