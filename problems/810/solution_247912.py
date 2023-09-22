def inverte(frase):
    frase=str.replace(frase,"-"," ")
    frase=str.replace(frase,","," ")
    frase=str.replace(frase,":"," ")
    frase=str.replace(frase,";"," ")
    frase=str.replace(frase,"."," ")
    frase=str.replace(frase,"!"," ")
    frase=str.replace(frase,"?"," ")
    frase=str.replace(frase,"."," ")
    frase=str.lower(frase)
    frase=list.split(frase," ")
    list.sort(frase, reverse=True)
	return frase