def inverte(frase):
    """Retorna uma frase com as palavras na ordem inversa da 
    frase de entrada, sem pontuacao e sem letras maiusculas dado:
    a frase de entrada"""
    
    fraseE=str.replace(frase,'-',' ')
    fraseE=str.replace(fraseE,',','')
    fraseE=str.replace(fraseE,':','')
    fraseE=str.replace(fraseE,';','')
    fraseE=str.replace(fraseE,'.','')
    fraseE=str.replace(fraseE,'!','')
    fraseE=str.replace(fraseE,'?','')
    fraseE=str.lower(fraseE)
    
    espaco=str.split(fraseE," ")
    inverte=espaco[::-1]
    fraseInvertida=str.join(" ",inverte)
    return fraseInvertida