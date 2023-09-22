def uppCons(frase):
    """Função que recebe uma frase de entrada e retorna a frase com as consoantes em maiusculo
    str -> str"""
    i=0
    consoante=''
    while i<len(frase):
        if frase[i] in "bcdfghjklmnpqrstvwxyzç":
            
            consoante = consoante + frase[i].upper()
        else:
            consoante = consoante + frase[i]
        i=i+1
	return consoante