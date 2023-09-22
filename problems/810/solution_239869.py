def sub(texto):
    frases= texto.replace("!", " ").replace("?", " ").replace(".", " ").replace(","," ").replace(":"," ").replace(";"," ").replace("-", " ")
    return frases