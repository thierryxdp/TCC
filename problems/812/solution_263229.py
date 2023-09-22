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