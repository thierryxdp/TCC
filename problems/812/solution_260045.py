def retira_pontuacao(texto):
    if "-", or ",", or ":", or ";" in texto:
        texto=texto.replace("-"," ")
        texto=texto.replace(","," ")
        texto=texto.replace(":"," ")
        texto=texto.replace(";"," ")
        return texto
    	else:
            return texto