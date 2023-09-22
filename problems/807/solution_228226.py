def conta_frases(frase):
    teste1 = str.count(frase, "!")
	teste2 = str.count(frase, "?")
    teste3 = str.count(frase, ".")
    teste4 = str.count(frase, "...") - 3
    
    return teste1 + teste2 + teste3 + teste4