def inverte(frase):
    """Funcao que, dada uma frase, retorna uma outra que contenha as mesmas palavras dela na ordem inversa, sem letras maiusculas e sem a pontuacao
       str-> str"""
    for caractere in ["-", ",", ":", ";", ".", "!", "?", "..."]:
        frase = str.replace(frase, caractere, " ")
        
    lista= str.split(frase)
    lista.reverse()
    frase=str.join(" ", lista)
    return frase