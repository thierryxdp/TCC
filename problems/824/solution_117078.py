def uppCons(frase):
    '''retorna as consoantes da frase como maiusculas
    str->str'''
    i=0
    consoantes=['b','c','ç','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    while i<22:
    	frase=frase.replace(consoantes[i],consoantes[i].upper())
        i+=1
    return frase