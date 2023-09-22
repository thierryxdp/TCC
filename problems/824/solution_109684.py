def uppCons(frase):
    """Função que recebe como entrada uma frase e retorna a frase com 
       todas as suas consoantes em maiúscula e os demais caracteres 
       exatamente como estavam na frase original.
       str->str
       
       Parâmetros:
       frase: A frase que será passada para a função.
       
       Returns: A frase com todas as suas consoantes em maiúscula e os 
                demais caracteres exatamente como estavam na frase 
                original.
    """
    contador = 0
    novafrase = ""
    while contador < len(frase):
        if frase[contador] == (str.lower(frase[contador])) in ('a','e','i','o','u'):
            return novafrase + frase[contador]
        else:
            return novafrase + str.upper(frase[contador])
        contador = contador + 1
    return novafrase