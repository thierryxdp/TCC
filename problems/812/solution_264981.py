def retira_pontuacao (frase):
    '''
       Dada uma frase a função retorna a mesma frase porém 
       sem pontuação
       str -> str
    '''
    if '.' in frase:
        str.replace('.', '')
    elif '!' in frase:
        str.replace('!', '')
    elif '?' in frase:
        str.replace('?', '')
    elif ',' in frase:
        str.replace(',', '')
    elif ':' in frase:
        str.replace(':', '')
    elif ';' in frase:
        str.replace(';', '')
    elif '...' in frase:
        str.replace('...', '')
    elif '-' in frase:
        str.replace('-', '')
        return frase