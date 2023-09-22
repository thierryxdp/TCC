def inverte(frase):
    frase=frase.replace("!"," ").replace(","," ").replace(":"," ").replace(";"," ").replace("."," ").replace("?"," ").replace("!"," ").replace("-"," ") and str.low(frase)
   	return str.join(str.spit(frase," ")," ",[:-1])