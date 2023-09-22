def conta_frases(frase):
    """A função analisa os pontos de exclamação, interrogação, ponto final e reticências, separando as frases em listas e calculando o numero de termos;
       str -> int"""
    frase1 = frase.replace("...","!")
    frase2 = frase1.replace("?","!")
    frase3 = frase2.replace(".","!")
    return len(frase3.split('!'))-1