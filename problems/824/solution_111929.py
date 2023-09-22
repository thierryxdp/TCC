def uppCons(frase):
    '''Retorna a frase com suas consoantes maiúsculas.
    str --> str'''
    i = 0
    j = 0
    fraseFinal = []
    consoantes = ['b','c','ç','d','e','f','g','h','j','k','l','m','n','o','p','q','r','s','t','v','w','x','y','z']
    vogal = True
    while(i < len(frase)):
        while(j < len(consoantes)):
        	if consoantes[j] in frase[i]:
			    fraseFinal[len(fraseFinal):len(fraseFinal)] = [str.upper(frase[i])]
            	j = len(consoantes)
                vogal = False
                
            if vogal:
                fraseFinal[len(fraseFinal):len(fraseFinal)] = [frase[i]]
        j = 0
        i += 1
    
	fraseFinal = str.join('',fraseFinal)
    return fraseFinal