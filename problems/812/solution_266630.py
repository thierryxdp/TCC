def retira_pontuacao(frase):
    """ retorna uma nova frase onde todos os caracteres de pontuaçãos serão substituídos por espaço,dado uma frase str-->str"""
    y=frase.replace(","," ")
    x=y.replace("."," ")
    z=x.replace(":"," ")
    a=z.replace("-"," ")
    b=a.replace(";"," ")
    c=b.replace("!"," ")
    d=c.replace("?"," ")
    return d