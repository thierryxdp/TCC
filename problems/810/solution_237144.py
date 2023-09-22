def inverte(frase):
    """Dada uma frase retorna outra que contenha as mesmas palavras na ordem inversa,
       sem letras maiúsculas e sem pontuação.
       str -> str"""
    
    for char in ".!?,:-;":
        frase = frase.replace(char, " ")
        
        return str.split(frase)[::-1]