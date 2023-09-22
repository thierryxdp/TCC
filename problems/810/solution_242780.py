def retira_pontuacao(frase):
    '''Função que retorna texto sem pontuação.
    str->str'''
    if '-'in frase:
        frase=str.replace(frase,'-',' ')
    if ',' in frase:
        frase=str.replace(frase,',',' ')
    if ':' in frase:
        frase=str.replace(frase,':',' ')  
    if ';' in frase:
        frase=str.replace(frase,';',' ')
    if '...' in frase:
        frase=str.replace(frase,'...',' ')
    if '?' in frase:
        frase=str.replace(frase,'?',' ')
    if '!' in frase:
        frase=str.replace(frase,'!',' ')
    if '.' in frase:
        frase=str.replace(frase,'.',' ')
    return frase

def inverte(frase):
    '''Retorna frase inserida sem pontuação em letra minúscula e com as palavras na ordem inversa.
    str->str'''
    frase=retira_pontuacao(frase)
    frase=str.lower(frase)
    palavras=str.split(frase)
    list.reverse(palavras) #invertendo ordem das palavras
    frase_inversa=str.join(' ',palavras)
    return frase_inversa