def uppCons(frase):
    i=0
    resultado=""
    while i<len(frase):
        
        if frase[i] in "ÂÃÁÀAÊÈÉEÎÌÍIÔÕÒÓOÛÙÚUâàáãaêèéeîìíiôòóõoûùúu":
        	resultado=resultado+frase[i]
        else:
            resultado=resultado+frase[i].upper()
        i=i+1
    return resultado