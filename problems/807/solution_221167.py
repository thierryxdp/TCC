def conta_frases(frases):
    """Retorna a quantidade de frases que aparecem no texto,
	que são separadas por '...', '!', '.', '?'; 
	str -> int """
    frase1 = str.split(frases,'...')
    novafrase = ''.join(frase1)
    ponto = str.split(novafrase,'.')
    interrogacao = str.split(frases,'?')
    exclamacao = str.split(frases,'!')
    
    return len(frase1)+len(ponto)+len(interrogacao)+len(exclamacao)