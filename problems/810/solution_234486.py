def retira_pontuacao(frase):
    """retira a pontuação de uma frase"""
    frase=frase.replace(";","#")
    frase=frase.replace("!","#")
    frase=frase.replace("?","#")
    frase=frase.replace(".","#")
    frase=frase.replace(":","#")
    frase=frase.replace(",","#")
    frase=frase.replace("-","#")
    s=str.replace(frase,"#"," ")
    return s

def inverte(frase):
    """inverte a frase de entrada"""
    retira_pontuacao(frase)
    str.split(frase)
    str.join(frase)
    return frase