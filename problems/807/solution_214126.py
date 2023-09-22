def altera_frase(frase, palavra, pos):
    palavras = str.split(frase)
	if palavra in palavras:
        idx = list.index(palavras, palavra)
        palavras[idx] = str.upper(palavra)
    else:
        list.insert(palavras, pos, palavra)
    
    return str.join(" ", palavras)