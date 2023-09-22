def conta_frases(frase):
    teste1 = str.count(frase, "!")
	teste2 = str.count(frase, "?")
    teste3 = str.count(frase, ".")
    teste4 = str.count(frase, "...") 
    
    contagem_bruta = teste1 + teste2 + teste3 + teste4
    
    if teste3 >= 1 and teste4 >= 1:
        return contagem_bruta - 3*teste4
    else:
        return contagem_bruta