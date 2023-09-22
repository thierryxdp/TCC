def inverte(frase):
    sub=frase.replace("!", " ").replace("?", " ").replace(".", " ").replace(","," ").replace(":"," ").replace(";"," ").replace("-", " ")
    normal=str.split(sub(frase),' ')
    invertida=normal[::-1]
    invtxt=str.join(' ',invertida)
    return invtxt.lower()