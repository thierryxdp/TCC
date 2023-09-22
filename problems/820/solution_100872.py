def posLetra(string,letra,num):
    letras=[]
    i=0
    while i<len(string):
        i+=1
    counter=1
    incidencia=0
    while counter <=len(string):
        if letras[counter-1]==letra:
            incidencia==num:
                return counter
        counter+=1
        
    return -1