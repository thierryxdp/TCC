def posLetra(Frase,Letra,Numero):
    contador = 0
    while contador <= Numero:
        if Numero <= Frase.count(Letra):
        	str.replace(Frase,Letra,'.',Numero-1)
        	Local = str.find(Frase, Letra)
        	contador = contador + 1
        else:
            Local = '-1'
            contador = contador + 1
	
    return Local