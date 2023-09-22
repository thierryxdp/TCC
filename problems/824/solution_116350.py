def uppCons(frase):
    """função que recebe uma frase(str) e retorna essa mesma frase (str) com as consoantes maiúsculas"""
    posicao = 0
    frasenova = ""
    while posicao < len(frase):
        if frase[posicao] in ["a","e","i","o","u",'á","à","â","ã","é","ê","í","ó","õ","ô","ú"]:
			      frasenova += frase[posicao]
           else:
			      frasenova += str.upper(frase[posicao])
    return frasenova