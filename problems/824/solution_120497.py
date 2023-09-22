#dado uma str retorna a frase original com suas consoantes maiúsculas
#str-->str
def uppCons(frase):
	s = ''
    for caractere in frase:
        if caractere in 'bcdfghjklmnpqrstvxwyzç':
            s += caractere.upper() 
        else: 
            s += caractere
    return s