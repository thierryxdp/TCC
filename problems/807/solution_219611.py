def conta_frases(frase):
    """Função que conte e retorna o número de frases que aparecem neste 
    texto
    str-> int"""
    
    f1 = frase.count(".")
    f2 = frase.count("!")
    f3 = frase.count("?")
    f4 = frase.count("...")
    if "..." in frase:
        return f1+f2+f3+f4-(3*f4)
	
	return f1+f2+f3+f4