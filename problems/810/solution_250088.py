def inverte(x=""):
    '''função que substitui pontuações por espaços na frase, inverte a ordem
    da frase e remove letras maiúsculas nela'''
    x=x.replace("."," ").replace(";"," ").replace(","," ").replace("-"," ").replace(":"," ").replace("?"," ").replace("!"," ").replace("/"," ")
    x=inverte(x).lower()
    x=x.split(" ")
    return str(" ").join(x[::-1])
    return x