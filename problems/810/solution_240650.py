def inverte(texto:str)->str:
    #essa função retira a pontuação de um texto
    texto=texto.replace(","," ")
    texto=texto.replace(":"," ")
    texto=texto.replace("."," ")
    texto=texto.replace("!"," ")
    texto=texto.replace("-"," ")
    texto=texto.replace("?"," ")
    texto=texto.lower()
    texto=texto.split(" ")
    inverso=[str.join(" ",texto)] 
    return inverso[-1::-1]