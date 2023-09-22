def retira_pontuacao(frase):
    """Função que substitui  os caracteres de pontuação por espaço
    str->str"""
    return frase.replace(".", " ").replace("!"," ").replace("-"," ").replace(":"," ").replace(";"," ").replace("?"," ").replace(","," ")

def inverte(frase):
    """..."""
    b = retira_pontuacao(frase)
    x = str.lower(b)
    a = list(str.split(x))
    y = a.reverse()
    return str.join(" ",a)