def retira_pontuacao (frase):
    '''Função que recebe uma frase (frase) e retorna a mesma
    frase com os caracteres de pontuação substituidos por
    espaço;
    
    '''
    frase.replace('.',' ')
    frase.replace('...',' ')
    frase.replace('!',' ')
    frase.replace('?',' ')
    frase.replace('-',' ')
    frase.replace(',',' ')
    frase.replace(':',' ')
    frase.replace(';',' ')
    return frase