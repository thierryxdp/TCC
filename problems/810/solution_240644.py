def inverte(texto:str)->str:
    #essa função retira a pontuação de um texto
    texto=texto.replace(",","")
    texto=texto.replace(":","")
    texto=texto.replace(".","")
    texto=texto.replace("!","")
    texto=texto.replace("-","")
    texto=texto.replace("?","")
    texto=texto.lower()
    texto=texto.split(" ")
    inverso=texto.join(" ") 
    return inverso[-1::-1]