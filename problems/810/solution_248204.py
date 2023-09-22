def inverte(frase):
    """Funçao que, dada uma frase, retorne uma outra frase que contenha
as mesmas palavras dessa frase na ordem inversa, 
sem letras maiusculas e sem pontuaçao"""
    frase=str.replace(frase,"-"," ")
    frase=str.replace(frase,","," ")
    frase=str.replace(frase,":"," ")
    frase=str.replace(frase,";"," ")
    frase=str.replace(frase,"."," ")
    frase=str.replace(frase,"!"," ")
    frase=str.replace(frase,"?"," ")
    frase=str.replace(frase,"..."," ")
    frase=str.lower(frase)
    frase=str.split(frase)
    inverte=" ".join(frase[::-1])
    return inverte