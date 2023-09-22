def invertida(x=""):
    x=x.replace("."," ").replace(";"," ").replace(","," ").replace("-"," ").replace(":"," ").replace("?"," ").replace("!"," ").replace("/"," ")
    x=x.split(" ")
    return str(" ").join(x[::-1])