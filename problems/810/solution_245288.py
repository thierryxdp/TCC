def retira_pontuacao(frase):
    """retorna a frase onde todos os caracteres de pontuação tenham sido substituidos por espaços; str -> str"""
    x=str.replace(frase,'-',' ')
    y=str.replace(x,',',' ')
    z=str.replace(y,':',' ')
    w=str.replace(z,';',' ')
    a=str.replace(w,'.',' ')
    b=str.replace(a,'!',' ')
    c=str.replace(b,'?',' ')
    d=str.replace(c,'...',' ')
    return d
def inverte(frase):
    """retorna outra frase que contenha as mesmas palavras da frase de entrada na ordem inversa sem letras maiusculas e sem pontuaçao; str -> str"""
    x=retira_pontuacao(frase)
    y=str.lower(x)
    z=str.split(y,' ')
    w=list.reverse(z)
    return w