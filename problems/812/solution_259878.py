def retira_pontuacao(frase):
    '''Retorna uma frase com os caracteres de pontuação 
    substituídospor espaços
    string -> string '''
    frase=frase.replace('-',' ')
    frase=frase.replace(':',' ')
    frase=frase.replace(';',' ')
    frase=frase.replace(';',' ')
    frase=frase.replace('.',' ')
    frase=frase.replace('!',' ')
    frase=frase.replace('?',' ')
    frase=frase.replace(',',' ')
    return frase