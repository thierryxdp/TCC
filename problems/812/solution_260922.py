def retira_pontuacao(frase):
    '''
    tira as pontuacoes de uma frase e substitui por espaco
    str -> str
    '''
    if '.' in frase and '!' in frase:
        return frase.replace('.',' ') and frase.replace('!',' ')