def retira_pontuacao (frase):
    '''Recebe uma frase e retorna a mesma sem pontuação, tendo um espaço 
    no lugar desta (str -> str)(pontuação:'-',',',':',';','.','?'e'!')'''
    frase = frase.replace('-',' ')
    frase = frase.replace(',',' ')
    frase = frase.replace(':',' ')
    frase = frase.replace(';',' ')
    frase = frase.replace('.',' ')
    frase = frase.replace('?',' ')
    frase = frase.replace('!',' ')
    return frase