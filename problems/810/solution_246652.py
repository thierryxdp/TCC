def inverte(texto:str)->str:
    """Retira as pontuações que aparecem em um texto, os subistituindo por espaço, invertendo as palavras de posição."""
    texto = texto.replace('...','.')
    texto = texto.replace('.','')
    texto = texto.replace('?','')
    texto = texto.replace('!','')
    texto = texto.replace(',','')
    texto = texto.replace(':','')
    texto = texto.replace(';','')
    texto = texto.replace('-',' ')
    ltexto = texto.lower()
    stexto = ltexto.split()
    inverttext = stexto[::-1]
    return  ' '.join(inverttext)