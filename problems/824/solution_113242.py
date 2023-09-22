def uppCons(frase):
    i = 0
    texto2=''
    while i < len(frase):
        if frase[i] == 'a': 
            texto2 = texto2 + frase[i]
        elif frase[i] == 'e':
            texto2 = texto2 + frase[i]
        elif frase[i] == 'i':
            texto2 = texto2 + frase[i] 
        elif frase[i] == 'o':
            texto2 = texto2 + frase[i]
        elif frase[i] == 'u':
            texto2 = texto2 + frase[i]
        
        
        else:
            texto2 = texto2 + str.upper(frase[i])
        i = i +1
        
    return texto2