def retira_pontuacao(frase):
    """calculo e retorno de uma funcao que retorne a frase onde os caracteres de pontuacao de pontuacao tenham sido substituidos por espaço"""
    x=frase
    b= str.replace(x,'!',' ')
    c=str.replace(b,'.',' ')
    d=str.replace(c,'?',' ')
    e=str.replace(d,',',' ')
    f=str.replace(e,'-',' ')
    return f