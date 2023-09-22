import retira_pontuacao
def inverte (frase):
    '''função que dada uma frase retorna uma outra frase com as mesmas palavras
    da frase original na ordem inversa, sem letras maiúsculas e sem pontuação;
    str -> str'''
    if '.' or '!' or '?' or '...' or '-' or ',' or ':' or ';' in frase:
        frase = retira_pontuacao(frase)
    return str.join(' ',str.split(str.lower(frase)))[::-1]