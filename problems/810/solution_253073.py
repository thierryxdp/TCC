def inverte(texto=""):
    '''Funcao que inverte uma frase dada, sem as letras maiusculas e pontuacao
    Str -> Str'''
    texto=texto.replace("."," ").replace(";"," ").replace(","," ").replace("-"," ").replace(":"," ").replace("?"," ").replace("!"," ")
    texto=texto.split(" ")
    return str(" ").join(texto[::-1])