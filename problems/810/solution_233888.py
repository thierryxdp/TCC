def inverte(frase):
    '''FUnção que inverte a ordem das palavras dadas em uma determinada frase como variável.
    string ->string'''

    frase = str.upper(frase)
    frase = str.replace(frase,".", " ")
    frase = str.replace(frase,",", " ")
    frase = str.replace(frase,":", " ")
    frase = str.replace (frase,"-"," ")
    frase = str.replace(frase,";"," ")
    frase = str.replace(frase,"!"," ")
    frase = str.replace(frase,"?"," ")
    SepararFrase = str.split(frase)
    
    return str.join(" ",(SepararFrase[::-1]))