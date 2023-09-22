def retira_pontuacao(frase):
    '''calcula uma função que dada uma frase,retorna a frase com todos os caracteres de pontuação substuídos por espaço;
    str-->str.'''
    novafrase = (frase.replace('-',' ').replace(',',' ').replace(':',' ').replace(';',' ').replace('.',' ').replace('?',' ').replace('!',' '))
    return novafrase