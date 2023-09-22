def uppCons(frase):
    '''função que retorna uma frase com todas as suas consoantes em maiúsculo, dado uma frase original'''
    i=0
    consoantes=""
    while i<len(frase):
        letra=frase[i]
        if letra in"aeiou":
            consoantes += str(letra)
            else:
                consoantes += str(letra.upper())
         i=i+1
        
	return consoantes