def uppCons(frase:str)->str:
    """ A funcao recebe como entrada uma frase, e retorna a frase com todas as suas consoantes em maiusculas, e os demais caracteres exatamente como estavam na frase original""" 
    resposta = ""
    indice = 0
    while (indice < len(frase)):
        if frase[indice] != 'aeiou':
            resposta += str.upper(str(frase[indice])) 
        else:
            resposta += str(frase[indice],)
            indice += 1 
    return frase