def retira_pontuacao (frase):
    '''
       Dada uma frase a função retorna a mesma frase porém 
       sem pontuação
       str -> str
    '''
    if '.' in frase:
        str.replace(frase,'.', '')
    elif '!' in frase:
        str.replace(frase,'!', '')
    elif '?' in frase:
        str.replace(frase,'?', '')
    elif ',' in frase:
        str.replace(frase,',', '')
    elif ':' in frase:
        str.replace(frase,':', '')
    elif ';' in frase:
        str.replace(frase,';', '')
    elif '...' in frase:
        str.replace(frase,'...', '')
    elif '-' in frase:
        str.replace(frase,'-', '')
        return frase