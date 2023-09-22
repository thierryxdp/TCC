def inverte(frase):
    """funcao que dada uma frase retorne uam outra frase com as mesmas palavras porem de tras para frente, sem letras maiusculas ou pontuacao"""
	"""str->str"""
    filtro1 = str.replace(frase,'-',' ')
    filtro2 = str.replace(filtro1,'.',' ')
    filtro3 = str.replace(filtro2,',',' ')
    filtro4 = str.replace(filtro3,'!',' ')
    filtro5 = str.replace(filtro4,'?',' ')
    filtro6 = str.lower(filtro5)
    filtro7 = str.split(filtro6)
    filtro8 = filtro7 [::-1]
    filtro9 = str.join(' ', filtro8)
    
    return filtro9