def inverte(frase):
    """Dada uma frase, retorna uma frase inversa com a mesmas
    palavras, sem maiúsculas e pontuação;
    str -> str"""
    resultado = str.replace(frase,"!"," ")
    resultado = str.replace(resultado,"."," ")
    resultado = str.replace(resultado,";"," ")
    resultado = str.replace(resultado,":"," ")
    resultado = str.replace(resultado,","," ")
    resultado = str.replace(resultado,"?"," ")
    resultado = str.replace(resultado,"-"," ")
    resultado = str.lower(resultado)
    resultado = str.strip(resultado)
    resultado = resultado[-1:]
    
    return resultado