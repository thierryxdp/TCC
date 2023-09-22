def inverte(frase):
    ''''Dado uma frase, retorna a frase em ordem inversa, sem letras maiusculas
    e pontuação.str -> str'''
    frase = str.replace(frase,"!"," ")
    frase = str.replace(frase,"?"," ")
    frase = str.replace(frase,"..."," ")
    frase = str.replace(frase,"."," ")
    frase = str.replace(frase,"-"," ")
    frase = str.replace(frase,","," ")    
    frase = str.replace(frase,":"," ")
    frase = str.replace(frase,";"," ")
    frase[::-1]
    
    
    return str.lower(frase)