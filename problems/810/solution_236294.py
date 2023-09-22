def inverte(frase):
    """Dada uma frase retorna a mesma com suas palavras na ordem contrária.
       Retorna também tudo em letras minúsculas e sem pontuação.
       str -> str"""
    
    for char in ".!?,:-;":
        frase = frase.replace(char, " ")
    return frase.split()