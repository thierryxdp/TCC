def uppCons(frase):
    i=0
    consoantes=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    while i<21:
    	frase.replace(consoantes[i],consoantes[i].upper())
        i+=1
    return frase