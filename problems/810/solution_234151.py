def inverte(x):
    """Função que inverte uma frase, sem pontuações e letras maiúsculas ; str --> str"""
    x = str.replace(x,"-"," ")
    x = str.replace(x,","," ")
    x = str.replace(x,":"," ")
    x = str.replace(x,";"," ")
    x = str.replace(x,"."," ")
    x = str.replace(x,"!"," ")
    x = str.replace(x,"?"," ")
    x = str.split(x) [-1::-1]
    x = str.join(" ",x)
    return str.lower(x)