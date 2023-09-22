def retira_pontuacao(frase):
    '''
    Função que dada uma frase, retorna a mesma frase
    com remoção de todas as pontuações das frases.
    
    str->str
    '''
    str.replace(frase,'.',' ', -1) or str.replace(frase,'!',' ') or str.replace(frase,'?',' ')or str.replace(frase,'-',' ') or str. replace(frase,',',' ')
    
    return frase