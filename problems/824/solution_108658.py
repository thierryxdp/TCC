def uppCons(frase):
    cont = 0
    contCons = 0
    check = False
    consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
                  'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y',
                  'z']
    
    while cont < len(frase):
        while contCons < 20 and check == False:
            if frase[cont] == consoantes[contCons]:
                frase[cont] = frase[cont].upper()
                check = True
            
            contCons += 1
       	
        cont += 1
        
	return frase