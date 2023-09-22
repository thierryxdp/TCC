def inverte(frase):
    """retorna uma frase com contenha as mesmas palavras da frase de entrada na ordem inversa,sem letras maiúsculas,e sem pontuação.
    Parametro:
    Entrada:str
    Saida:str"""
    frase=frase.replace("!","").replace(",","").replace(":","").replace(";","").replace(".","").replace("?","").replace("!","").replace("-"," ")
    frase=frase.lower()
    return str.join(" ",str.split(frase," ")[::-1])