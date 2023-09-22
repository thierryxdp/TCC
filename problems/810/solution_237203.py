def inverte(frase):
    """Dada uma frase retorna outra que contenha as mesmas palavras na ordem inversa,
       sem letras maiúsculas e sem pontuação.
       str -> str"""
    
   
    frase1 = str.lower(frase) 
    
    for char in "!":
        frase2 = frase1.replace(char, " ")
        
    for char in "-":
        frase3 = frase2.replace(char, " ")
        
    for char in "?":
        frase4 = frase3.replace(char, " ")
        
    for char in ",":
        frase5 = frase4.replace(char, " ")
        
    for char in ".":
        frase6 = frase5.replace(char, " ")
        
        
        return " ".join(str.split(frase6)[::-1])