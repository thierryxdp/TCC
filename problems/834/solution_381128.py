def media_matriz(m):
    soma=0
    i=0
    x=0
    
    if len(m)!=0:
    	while i<len(m):
            soma+=sum(m[1])
            x+=len(m[1])
            i+=1
    media=soma/x
    return round(media,2)