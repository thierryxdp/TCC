def retira_pontuacao(frase):
    '''
    Função que dada uma frase, retorna a mesma frase
    com remoção de todas as pontuações das frases.
    
    str->str
    '''
    frase= frase.replace('.',' ')
    frase=frase.replace('!',' ') 
    frase=frase.replace('?',' ')
    frase=frase.replace('-',' ') 
    frase= frase.replace(',',' ')
    frase= frase.replace(':',' ')
    frase= frase.replace(';',' ')
    
    return frase