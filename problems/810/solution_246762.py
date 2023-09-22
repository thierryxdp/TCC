def retira_pontuacao(frase):
    """
    função que, dada uma frase, retorna a mesma sem pontuação.
    """
    
    x=frase
    x=str.replace(x,'!',' ')
    x=str.replace(x,'...',' ')
    x=str.replace(x,'?',' ')
    x=str.replace(x,'.',' ')
    x=str.replace(x,'-',' ')
    x=str.replace(x,',',' ')
    x=str.replace(x,':',' ')
    x=str.replace(x,';',' ')
    
    return x

def inverte(frase):
    """
    dada uma frase, retorna uma outra frase com as mesmas palavras em
    ordem inversa.
    """
    
    frase2=retira_pontuacao(frase)
    y=str.split(frase2)
    list.reverse(y)
    frase2=str.join(' ',y)
    frase2=str.lower(frase2)
    return frase2