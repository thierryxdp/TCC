#dado uma str retorna a frase original com suas consoantes maiúsculas
#str-->str
def uppCons(t):
	 s = ''
    for caractere in frase:
        if caractere in 'bcdfghjklmnpqrstvxwyz':
            s += caractere.upper() # transforma em maiúscula
        else: # não é consoante minúscula, mantém como no original
            s += caractere
    return s