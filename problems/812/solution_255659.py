def retira_pontuacao(frase):
    """Retorna a frase dada sem pontuação
       Entrada: str
       Saida: str
    """
    x=str.replace(frase,'/',' ')
    x=str.replace(x,'!',' ')
    x=str.replace(x,'?',' ')
    x=str.replace(x,'...',' ')
    x=str.replace(x,',',' ')
    x=str.replace(x,'.',' ')
    x=str.replace(x,':',' ')
    x=str.replace(x,'-',' ')
    return x