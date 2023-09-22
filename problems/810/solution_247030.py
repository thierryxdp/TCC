def retira_pontuacao(frase):
    ''' retorna a frase com todos os caracteres de pontuacao
    substituidos por espaço; str->str'''
    if '-' in frase:
        frase= frase.replace('-',' ')
    if ',' in frase:
        frase= frase.replace(',',' ')
    if ':' in frase:
        frase= frase.replace(':',' ')
    if ';' in frase:
        frase= frase.replace(';',' ')
    if '.' in frase:
        frase= frase.replace('.',' ')
    if '?' in frase:
        frase= frase.replace('?',' ')
    if '!' in frase:
        frase= frase.replace('!',' ')
        
def inverte(frase):
    ''' '''
    frase=frase.split(' ')
    frase_invertida=frase[::1]
    return frase_invertida.lower(frase_invertida)