def uppCons(frase):
    """Retorna a frase recebida com todas as suas consoantes maiúsculas"""
    
    consoantes = ['q','w','r','t','y','u','p','s','d','f','g','h','j','k','l','ç','z','x','c','v','b','n','m']
    if frase in consoantes:
		frase = frase.replace(frase,frase.upper())
        
    return frase

	x = str(map(uppCons,frase))