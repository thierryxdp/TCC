def inverte(frase):
    frase=frase.replace("!"," ").replace(","," ").replace(":"," ").replace(";"," ").replace("."," ").replace("?"," ").replace("!"," ").replace("-"," ")
    frse=frase.lower()
    return str.join(" ",str.split(frase," ")[::-1])