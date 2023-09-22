def uppCons(frase):
    letras = 'aeiouAEIOU'
    palavras=''
    i=0
    while i<len (frase):
        if frase[i] not in letras:            
            palavras= palavras + str.upper(frase[i])
        else:
            palavras = palavras+ frase[i]
        i=i+1
    return palavras