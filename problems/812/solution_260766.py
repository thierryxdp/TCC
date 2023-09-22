def retira_pontuacao(frase):
    '''
    Função que dada uma frase, retorna a mesma frase
    com remoção de todas as pontuações das frases.
    
    str->str
    '''
    str.replace(frase,'.',' ')
    str.replace(frase,'!',' ') 
    str.replace(frase,'?',' ')
    str.replace(frase,'-',' ')
    
    return frase