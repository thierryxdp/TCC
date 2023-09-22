def quant_palavras(frase):
    #funcao que recebe uma frase e retorna o numero de palavras dela
    #str -> int
    
    frase = frase.strip()
    frase = frase.split()
    frase = len(frase)

    return frase