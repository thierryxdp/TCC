def retira_pontuacao(frase):
    """ retorna a frase onde todos os caracteres de pontuação tenham sido substituídos por espaço str-->str"""
    x=frase.replace(frase,","," ")
    y=x.replace(frase,"."," ")
    z=y.replace(frase,":"," ")
    a=z.replace(frase,"-"," ")
    b=a.replace(frase,";"," ")
    c=b.replace(frase,"!"," ")
    d=c.replace(frase,"?"," ")
    return d