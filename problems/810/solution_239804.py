def sub(frase): 
frases= frase.replace("!", " ").replace("?", " ").replace(".", " ").replace(","," ").replace(":"," ").replace(";"," ").replace("-", " ")
 
def inverte(frase):
    normal=str.split(sub(frase),' ')
    invertida=normal[::-1]
    invtxt=str.join(' ',invertida)
    return invtxt.lower()