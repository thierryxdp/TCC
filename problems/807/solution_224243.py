def conta_frases(frase):
    
    tamanho=str.split(str(frase),'. or ! or ? or ...')
    
    return len(tamanho)