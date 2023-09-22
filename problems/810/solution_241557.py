def inverte(frase):
    """A entrada é uma frase sem letras maiúsculas 
    contida dentro do parâmetro e o seu
    retorno será essa mesma frase com as palavras
    de trás para frase em relação a original, sendo que
    nesse retorno não terá pontuações"""
    #str -> list
    
    if "-" in frase:
        frase = frase.replace ("-", " ")
      
    if "." in frase:
        frase = frase.replace (".", " ")
        
    if "!" in frase:
        frase = frase.replace ("!", " ")
        
    if "?" in frase:
        frase = frase.replace ("?", " ")
        
    if "," in frase:
        frase = frase.replace (",", " ")
     
    frase = frase.split()
    frase = ' '.join(frases[::-1]
    frase.reverse()
    
                         return frase.lower()