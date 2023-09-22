def conta_frases(texto):
    """Função conta quantas frases tem uma string;
str -> int"""
    contagem = 0 
    frase1 = str.split(texto, "!")
    del frase1[len(frase1)-1]
    contagem += len(frase1) 
    frase2 = str.split(texto, "?")
    del frase2[len(frase2)-1]
    contagem += len(frase2)
    frase3 = str.replace(texto, "...", ".")
    contagem += str.count(frase3, ".")
    
    return contagem