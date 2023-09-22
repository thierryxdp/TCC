def posLetra(frase,letra,num):
    i = 0
    ocorrencias = 0
    if (letra in frase):
    	while (ocorrencias < num):
            if (frase[i] == letra):
                ocorrencias = ocorrencias + 1
            i = i + 1
        return i - 1
    elif ocorrencias < num:
		return - 1
    else:
        return - 1