def invertida(x=""):
    '''função que dada uma frase retorna outra frase com as mesmas quantidades de palavras'''
    x=x.replace("."," ").replace(";"," ").replace(","," ").replace("-"," ").replace(":"," ").replace("?"," ").replace("!"," ").replace("/"," ")
    x=x.split(" ")
    return str(" ").join(x[::-1])