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

def inverte(frase):
    """Retorna a frase dada invertida
       Entrada: str
       Saida: str
    """
    x=retirada_pontuacao(frase)
    x=str.lower(x)
    x=str.split(x)
    x=x[::-1]
    x=str.join(' ',x)
    return x