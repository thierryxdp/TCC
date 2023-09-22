def uppCons (frase):
    'dada uma frase, retorna-a com as consoantes em caixa alta.
      str -> str'
    	a = 0
        s = ' '
        while a < len(frase):
            if frase[a] in '-aeiouAEIOU!?,.;:ÀÁÉÍÓÚÕáàéóíúõ~ãÃâÂêîÎôÔ':
                s = s + frase[a]
            elif frase[a] in ' bcdfghjlmnpqrstvxzywçBCDFGHJLMNPQRSTWUVXYZÇ':
                b = str.upper(frase[a])
                s = s + b
        	a += 1
    	return s[1::]