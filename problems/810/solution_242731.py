def retira_pontuacao(frase):
    frase=str.replace(frase,'-',' ')
    frase=str.replace(frase,',',' ')
    frase=str.replace(frase,':',' ')
    frase=str.replace(frase,';',' ')
    frase=str.replace(frase,'!',' ')
    frase=str.replace(frase,'?',' ')
    frase=str.replace(frase,'.',' ')
    frase=str.replace(frase,'...',' ')
    return frase

def inverte(frase):
    """dada uma frase, retorna outra frase com ordem
    iversa,sem letras maiusculas e sem pontuacao;
    str->str"""
    frase=retira_pontuacao(frase)
    frase=str.lower(frase)
    frase=str.split(frase)
    list.reverse(frase)
    frase=str.join(' ',frase)
    return frase