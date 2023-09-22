def retira_pontuacao (frase):
    '''Recebe uma frase e retorna a mesma sem pontuação, tendo um espaço 
    no lugar desta (str -> str)(pontuação:'-',',',':',';','.','?'e'!')'''
    if frase == '':
        return frase
    frase = frase.replace('-','',)
    frase = frase.replace(',','',)
    frase = frase.replace(':','',)
    frase = frase.replace(';','',)
    frase = frase.replace('.','',)
    frase = frase.replace('?','',)
    frase = frase.replace('!','',)
    return frase