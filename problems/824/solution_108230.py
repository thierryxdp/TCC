def uppCons(frase):
    i=0
    string = ""
    while i<len(frase):
        
        if frase[i] in "ÂÃÁÀAÊÈÉEÎÌÍIÔÕÒÓOÛÙÚUâàáãaêèéeîìíiôòóõoûùúu":
            string = string + frase[i]
            
        else:
            string = string + frase[i].upper()
            
        i=i+1
            
    return string