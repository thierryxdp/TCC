def uppCons(frase:str)->str:
    """ A funcao recebe como entrada uma frase, e retorna a frase com todas as suas consoantes em maiusculas, e os demais caracteres exatamente como estavam na frase original"""
    indice = 0
    resposta = ""
    while indice < len(frase):
           if frase[indice] in 'aeiou':
        resposta = frase[indice]
           else:
        resposta = str.strip(resposta,frase[indice])
           indice += 1
            
    return resposta