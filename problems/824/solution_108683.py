def uppCons(frase):
    cont = 0
    contCons = 0
    check = False
    consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
                  'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y',
                  'z', 'ç']
    frase = list(frase)
    
    while cont < len(frase):
        contCons = 0
        check = False
        while contCons < 22 and check == False:
            if frase[cont] == consoantes[contCons]:
                frase[cont] = frase[cont].upper()
                check = True
            
            contCons += 1
       	
    	cont += 1
        
    frase = ''.join(frase)
        
    return frase