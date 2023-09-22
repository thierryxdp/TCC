def retira_pontuacao(frase):
    '''funç˜ao que dada uma frase, retorne a frase onde todos os caracteres de pontuaç˜ao
    (incluindo travess˜ao, vírgula, dois pontos, ponto e vírgula, além da pontuaç˜ao de
    encerramento de frase) tenham sido substituídos por espaço.
    str->str.'''
    return str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,'!',' '),'.',' '),'?',' '),'-',' '),':',' '),';',' '),',',' '),'...',' ')