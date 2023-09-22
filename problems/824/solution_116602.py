def uppCons(frase):
    """Recebe uma frase e retorna a frase com todas as suas consoantes em 
    maiúsculas"""
    contador = 0
    while contador < len(frase):
        if frase[contador] in 'BbCcDdFfGHhgJjKkLlMmNnPpQqRrSsTtVvWwXxZzç':
            frase = frase.replace(frase[contador],frase[contador].upper())
        contador += 1
    return frase