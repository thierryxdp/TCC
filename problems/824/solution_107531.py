def uppCons(frase):
    i=0
    while i<len(frase):
        if frase[i]=="a" or frase[i]=="e" or frase[i]=="i" or frase[i]=="o" or frase[i]=="u":
            frase[i] = frase[i]

        else:
            frase[i] == str.upper(frase[i])
            
        i = i+1
            

    return frase