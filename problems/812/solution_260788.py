def retira_pontuacao(frase):
    '''
    Função que dada uma frase, retorna a mesma frase
    com remoção de todas as pontuações das frases.
    
    str->str
    '''
    frase.replace('.',' ')
    frase.replace('!',' ') 
    frase.replace('?',' ')
    frase.replace('-',' ') 
    frase.replace(',',' ')
    frase.replace(':',' ')
    frase.replace(';',' ')
    
    
    return frase