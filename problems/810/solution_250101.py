def inverte(x=""):
    '''função que substitui pontuações por espaços na frase, inverte a ordem
    da frase e remove letras maiúsculas nela'''
    a=x.replace("."," ").replace(";"," ").replace(","," ").replace("-"," ").replace(":"," ").replace("?"," ").replace("!"," ").replace("/"," ")
    b=inverte(a).lower(a)
    c=b.split(" ")
    d=str(" ").join(c[::-1])
    return d