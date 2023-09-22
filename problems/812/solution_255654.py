def retira_pontuacao(frase):
    """Retorna a frase dada sem pontuação
       Entrada: str
       Saida: str
    """
    x=frase.replace(frase,'.',' ')
    x=str.replace(frase,'!',' ')
    x=str.replace(frase,'?',' ')
    x= str.replace(frase,'...',' ')
    x= str.replace(frase,',',' ')
    return x