def retira_pontuacao(frase):
    """funçao que substitui todas as pontuaçoes por espaço
    str->str"""
    if '.' in frase:
        frase=frase.replace('.',' ')
    if '!' in frase:
        frase=frase.replace('!',' ')
    if '?' in frase:
        frase=frase.replace('?',' ')
    if '...' in frase:
        frase=frase.replace('...',' ')
    if ',' in frase:
        frase=frase.replace(',',' ')
    if '_' in frase:
        frase=frase.replace('_',' ')
        return frase