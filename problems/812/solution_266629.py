def retira_pontuacao(frase):
    """ retorna a frase onde todos os caracteres de pontuação tenham sido substituídos por espaço str-->str"""
    y=frase.replace(frase,","," ")
    x=y.replace("."," ")
    z=x.replace(":"," ")
    a=z.replace("-"," ")
    b=a.replace(";"," ")
    c=b.replace("!"," ")
    d=c.replace("?"," ")
    return d