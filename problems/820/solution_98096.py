def posLetra(frase,letra,num):
    """"""
    contador = 0
    pos = 0
    i = 0
    while i < len(frase):
        if frase.count(letra) < num:
            pos = -1
        else:
            if frase[i] == letra:
                contador += 1
                if contador == num:
                    pos = i
		i+=1
	return pos