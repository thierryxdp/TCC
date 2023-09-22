def media_matriz(m):
    soma=0
    i=0
    q=0
    
    if len(m)!=0:
    	while i<len(m):
            soma+=sum(m[1])
            q+=len(m[1])
            i+=1
    media=soma/q
    return(media,2)