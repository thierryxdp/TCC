def conta_frases(texto):
    """A função retorna a quantidade de frases em um determinado texto
    str-->int."""
    frase1 = len(str.split(texto,"."))
    frase2 = len(str.split(texto,"!"))
    frase3 = len(str.split(texto,"?"))
    frase4 = str.count(texto,"...")
    return (frase1  + frase2 + frase3 - 2 * frase4 -3)

def inverte(frase):
    """A função retorna uma outra frase que contenha as mesmas palavras
    da frase de entrada na ordem inversa, sem maiúscula, e sem a
    pontuação.
    str-->str."""
    
    lista_frase = frase.split(" ")
    posicao = len(lista_frase) + 1
    inverter = lista_frase[posicao:-(posicao): -1]
    concatenar = str.join(" ",inverter)
    
    return str.lower(concatenar)