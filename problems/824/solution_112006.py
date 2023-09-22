def uppCons(frase):
    cont = 0
    cont2 = 0
    frase2 = frase.split(' ')
    while (cont < len(frase2)):
        palavra = list(frase2[cont])
        
        while (cont2 < len(palavra)):
            
            if not (lower(palavra[cont2]) == 'a'
            or lower(palavra[cont2]) == 'e'
            or lower(palavra[cont2]) == 'i'
            or lower(palavra[cont2]) == 'o'
            or lower(palavra[cont2]) == 'u'):
        		palavra[cont2] = upper(palavra[cont2])
            
            cont2 = cont2 + 1
        frase2[cont] = palavra
        cont = cont + 1
    return frase2.join(' ')