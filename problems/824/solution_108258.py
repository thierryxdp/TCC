def uppCons (frase):
    	a = 0
        s = ' '
        while a < len(frase):
            if frase[a] in 'aeiouAEIOU!?,.;:ÀÁÉÍÓÚÕáàéóíúõ~ãÃâÂêîÎôÔ':
                s = s + frase[a]
            elif frase[a] in 'bcdfghjlmnpqrstvxzywçBCDFGHJLMNPQRSTWUVXYZÇ':
                b = str.upper(frase[a])
                s = s + b
        	i += 1
    	return s