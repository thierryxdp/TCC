def uppCons(frase):
    i = 0
    consoante = 'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','y','z'
    fraseNew = []
    while i < len(frase):
        if frase == consoante:
            frese = frase.replace(frase[i],frase.upper())
       	
        fraseNew = fraseNew + [frase[i],]   
	return fraseNew