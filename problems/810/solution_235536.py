def inverte(frase):
    """Funcao que, dada uma frase, retorna uma outra que contenha as mesmas palavras dela na ordem inversa, sem letras maiusculas e sem a pontuacao
       str-> str"""
    frase2=str.lower(frase[:])
    for caractere in ["-", ",", ":", ";", ".", "!", "?", "..."]:
        frase2= str.replace(frase2, caractere, " ")
        
        lista=str.split(frase2)
        lista.reverse()
        frase2=str.join(" ", lista)
        
        return frase2