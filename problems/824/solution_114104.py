def uppCons(frase):
    """Função que recebe como entrada uma frase e retorna-a com as consoantes em caixa alta."""
    """string->string"""
    i=0
    consoante="bcdfghjklmnpqrstvxwyz"
    while i<len(frase):
        if frase[i] in consoante:
            str.replace(frase[i],str.upper(frase[i]),-1)
        i=i+1
    return frase