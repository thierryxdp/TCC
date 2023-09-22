def retira_pontuacao(frase):
    """calculo e retorno de uma funcao que retorne a frase onde os caracteres de pontuacao de pontuacao tenham sido substituidos por espaço"""
    x=frase
    b= str.replace(x,'!',' ')
    c=str.replace(x,'.',' ')
    d=str.replace(x,'?',' ')
    e=str.replace(x,',',' ')
    f=str.replace(x,'-',' ')
    return b or c or d or e and f