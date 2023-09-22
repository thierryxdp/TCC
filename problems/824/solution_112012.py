def uppCons(frase):
    cont = 0
    cont2 = 0
    frase2 = frase.split(' ')
    while (cont < len(frase2)):
        palavra = list(frase2[cont])
        
        while (cont2 < len(palavra)):
            
            if not (palavra[cont2].lower == 'a'
            or palavra[cont2].lower == 'e'
            or palavra[cont2].lower == 'i'
            or palavra[cont2].lower == 'o'
            or palavra[cont2].lower == 'u'):
        		palavra[cont2] = palavra[cont2].upper
            
            cont2 = cont2 + 1
        frase2[cont] = palavra
        cont = cont + 1
	string = ' '.join(frase2)
    return string