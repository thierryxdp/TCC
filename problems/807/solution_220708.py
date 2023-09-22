def conta_frases(texto):
    "retorna o número de frases em um conjunto de frases"
    "str -> int"
    if "..." in texto:
    	frase=texto.replace("...",".")
    aux=0
    aux=aux+str.count(texto,".", 0)
    aux=aux+str.count(texto,"!",0)
    aux=aux+str.count(texto,"?",0)
    aux=aux+str.count(texto,"...",0)
    return aux