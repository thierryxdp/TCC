def inverte(texto:str)->str:
    """Retira as pontuações que aparecem em um texto, os subistituindo por espaço."""
    texto1 = texto.replace('...','.')
    texto2 = texto1.replace('.','')
    texto3 = texto2.replace('?','')
    texto4 = texto3.replace('!','')
    texto5 = texto4.replace(',','')
    texto6 = texto5.replace(':','')
    texto7 = texto6.replace(';','')
    texto8 = texto7.replace('-',' ')
    ltexto = texto8.lower()
    stexto = ltexto.split()
    return str(stexto[::-1])