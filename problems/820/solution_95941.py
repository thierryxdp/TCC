def posLetra(Frase,Letra,Numero):
    contador = 0
    while contador <= Numero:
        if Numero <= Frase.count(Letra):
            Local = str.find(Frase, Letra)
        	str.replace(Frase,str(Letra),'.',Numero-1)
        	contador = contador + 1
        else:
            Local = '-1'
            contador = contador + 1
	
    return  Local