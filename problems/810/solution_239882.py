def sub(texto):
    frases= texto.replace("!", "").replace("?", "").replace(".", "").replace(",","").replace(":"," ").replace(";","").replace("-", " ")
    return frases

def inverte(frase):
    "A Função inverte uma frase sem a pontuação e sem letras maiúsculas; str->str"""
    normal=str.split(sub(frase),' ')
    invertida=normal[::-1]
    invtxt=str.join(' ',invertida)
    return invtxt.lower()