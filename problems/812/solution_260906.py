def retira_pontuacao(frase):
    '''
    tira as pontuacoes de uma frase e substitui por espaco
    str -> str
    '''
    return frase.replace('—',' ')+frase.replace(',',' ')+frase.replace(':',' ')+frase.replace(';',' ')+frase.replace('.',' ')+frase.replace('...',' ')+frase.replace('!',' ')+frase.replace('?',' ')