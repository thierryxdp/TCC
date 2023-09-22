def consoante(frase):


    """Função que recebe uma string e retorna a string com todas as consoantes em maísculas."""
    #str -> str 


    contador = 0
    while contador < len(frase):
       
        if frase[contador] in 'BbCcDdFfGHhgJjKkLlMmNnPpQqRrSsTtVvWwXxZzç':
            frase = frase.replace(frase[contador],frase[contador].upper())
    
        contador += 1
    return frase