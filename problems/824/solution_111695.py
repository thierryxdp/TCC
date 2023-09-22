def uppCons(frase):
    '''função que retorna uma frase com todas as suas consoantes em maiúsculo, dado uma frase original'''
    i=0
    consoantes=""
    while i<len(frase):
        letras=frase[i]
        if letra in"aeiou":
            consoantes += str(letra)
        else:
            consoantes += str(letra.upper())
        
	return consoantes