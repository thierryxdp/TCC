def uppCons(frse):
    i=0
    resultado=""
    while i<len(frase):
        
        if frase[i] in "ÃÃÁÀAÊÈÉEÎÌÍIÔÕÒÓOÛÙÚUâàáãaêèéeîìíiôòóõoûùúu":
        	resultado=resultado+frase[i]
        else:
            resultado=resultado+frase.upper()
        i=i+1
    return resultado