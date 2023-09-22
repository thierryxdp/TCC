def retira_pontuacao(frase):
    '''
       Função que recebe uma frase e substitui todas as suas pontuações por espaço
       str --> str
    '''
    frase = frase.replace('-',' ')
    frase = frase.replace(',',' ')
    frase = frase.replace(':',' ')
    frase = frase.replace(';',' ')
    frase = frase.replace('.',' ')
    frase = frase.replace('?',' ')
    
    return frase