def inverte(texto:str)->str:
    #essa função inverte uma frase
    texto=texto.replace(",","")
    texto=texto.replace(":","")
    texto=texto.replace(".","")
    texto=texto.replace("!","")
    texto=texto.replace("-","")
    texto=texto.replace("?","")
    texto=texto.lower()
    texto=texto.split(" ")
    texto=texto[-1::-1]
    x=str.join(" ",texto) 
    return x[1:]