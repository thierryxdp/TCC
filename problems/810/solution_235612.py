def inverte(frase):
    frase=frase.replace("!"," ").replace(","," ").replace(":"," ").replace(";"," ").replace("."," ").replace("?"," ").replace("!"," ").replace("-"," ")
    return str.join(" ",str.split(frase," ")[::-1])