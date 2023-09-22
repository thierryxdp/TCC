def uppCons(frase):
    """Funcao que recebe uma frase e retorna a mesma frase so que com as consoantes maiusculas. str=>str"""
    frase1= ''
    x=0
    while x<len(frase):
        if frase[x] in 'BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwYyZz':
            frase1= frase1=str.upper(frase[x])
        else:
            frase1= frase1+frase1[x]
        x=x+1
    return frase1