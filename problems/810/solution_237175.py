def inverte(frase):
    """Dada uma frase retorna outra que contenha as mesmas palavras na ordem inversa,
       sem letras maiúsculas e sem pontuação.
       str -> str"""
    
   
    frase1 = str.lower(frase) 
    
    for char in "!.?,:;-":
        frase2 = frase1.replace(char, " ")
        
        return str.split(frase2)[::-1]