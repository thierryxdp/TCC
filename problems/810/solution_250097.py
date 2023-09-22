def inverte(x=""):
    '''função que substitui pontuações por espaços na frase, inverte a ordem
    da frase e remove letras maiúsculas nela'''
    x=x.replace("."," ").replace(";"," ").replace(","," ").replace("-"," ").replace(":"," ").replace("?"," ").replace("!"," ").replace("/"," ")
    a=inverte(x).lower()
    b=a.split(" ")
    c=str(" ").join(b[::-1])
    return c