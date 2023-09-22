def retira_pontuacao(frase):
    """funcao que retorna uma frase sem pontuacao, substituindo por espaco
    str -> str"""

    if '.' in frase:
        frase = frase.replace('.',' ')
    
    if '!' in frase:
        frase = frase.replace('!',' ')

    if '?' in frase:
        frase = frase.replace('?',' ')

    if '...' in frase:
        frase = frase.replace('...',' ')

    if '-' in frase:
        frase = frase.replace('-',' ')

    if ',' in frase:
        frase = frase.replace(',',' ')

    if ':' in frase:
        frase = frase.replace(':',' ')

    if ';' in frase:
        frase = frase.replace(';',' ')
    
    return frase