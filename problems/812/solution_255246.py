def retira_pontuacao(frase):
    """calculo e retorno de uma funcao que retorne a frase onde os caracteres de pontuacao de pontuacao tenham sido substituidos por espaço"""
    x=frase
    b= str.replace(x,'!',' ')
    c=str.replace(x,'.',' ')
    d=str.replace(x,'?',' ')
    e=str.replace(x,',',' ')
    f=str.replace(x,'-',' ')
    if '-' and '.' in x:
        return f
    elif '!' in x:
        return b
    elif '.' in x:
        return c
    elif '?' in x :
        return d
    elif ',' in x:
        return e