def uppCons(frase):
    i=0
    resultado=""
    while i<len(frase):
        if frase[i] in "aãeéiíoôùuAÃEÉIÍOÔUÙ":
            resultado = resultado + frase [i]
        else:
            resultado = resultado + str.upper(frase[i])
    	i+=1
    return resultado