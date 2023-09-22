def retira_pontuacao(frase):
    '''
    Parametros: frase
    entrada: str
    saida : str
    Funcao que retira a pontuacao
    
    
    '''
    
    
    if '-' in frase:
        frase = frase.replace('-',' ')
    if ',' in frase:
        frase = frase.replace(',',' ')
    if ';' in frase:
        frase = frase.replace(';',' ')
    if ':' in frase:
        frase = frase.replace(':', ' ')
    if '.' in frase:
        frase = frase.replace('.', ' ')
    if '?' in frase:
        frase = frase.replace('?',' ')
    if '!' in frase:
        frase = frase.replace('!', ' ')
    
    return frase