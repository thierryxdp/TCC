def inverte(frase):
#Traveção 
    frase = str.split(frase, '-')
    frase = str.join(" ", frase)
#Virgula
    frase = str.split(frase, ',')
    frase = str.join("", frase)
#dois pontos    
    frase = str.split(frase, ':')
    frase = str.join("", frase)
#Ponto e virgula
    frase = str.split(frase, ';')
    frase = str.join("", frase)
#Exclamação
    frase = str.split(frase, '!')
    frase = str.join("", frase)
#Interrogação
    frase = str.split(frase, '?')
    frase = str.join("", frase)
#Ponto final
    frase = str.split(frase, '.')
    frase = str.join("", frase)
#Separador
    frase = str.split(frase, ' ')
    frase = frase[::-1] 
    frase = str.join(" ", frase)
    frase = frase.lower()
    return frase