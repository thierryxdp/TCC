def uppCons(frase):
    """Retorna a frase recebida com todas as suas consoantes maiúsculas"""
    
    vogais = 'aeiouáéíóúãõ'
    if frase[i] not in vogais:
		frase = frase.replace(frase[i],frase[i].upper())
        
    return frase

	x = str(map(uppCons,frase))