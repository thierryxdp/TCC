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
    palavras_frase_inversa=list.reverse(palavras)
    frase_inversa=str.join(' ',palavras_frase_inversa)
    return frase_inversa