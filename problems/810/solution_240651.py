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
    texto=texto[-1::-1]
    texto=[str.join(" ",texto)] 
    return texto[-1::-1]