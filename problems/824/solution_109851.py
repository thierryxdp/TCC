def uppCons(frase):
    """Retorna a frase recebida com todas as suas consoantes maiúsculas"""
    
    vogais = 'aeiouáéíóúãõ'
    if frase not in vogais:
		frase = frase.replace(frase,frase.upper())
        
    return frase

frase = uppCons()
x = str(map(uppCons,frase))