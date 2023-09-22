def retira_pontuacao(frase):
    """calculo e retorno de uma funcao onde todos os caracteres de pontuacao sejam substituidos por espaço"""
    x=frase
    a= str.replace (x,'!',' ')
    b= str.replace(x,'.',' ')
    c= str.replace(x,',',' ')
    d= str.replace(x,'?',' ')
    if a!=b:
        return d
    if b!=a:
        return b
    if b!=c:
        return b
    if c!=d:
        return c