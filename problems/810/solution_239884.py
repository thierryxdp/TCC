def retira_pontuacao(frase):
    """Função que substitui  os caracteres de pontuação por espaço
    str->str"""
    return frase.replace(".", " ").replace("!"," ").replace("-"," ").replace(":"," ").replace(";"," ").replace("?"," ").replace(","," ")

def inverte(frase):
    """..."""
    x = str.lower(frase)
    str.split(x)
    y = x.reverse()
    return str.join(" ",y)