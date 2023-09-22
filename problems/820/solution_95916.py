def posLetra(Frase,Letra,Numero):
    contador = 0
    NumeroL = Numero-1
    while contador < NumeroL:
        if NumeroL <= Frase.count(Letra):
        	str.replace(Frase,'.',Letra)
        	Local = str.find(Frase, Letra)
        	contador = contador + 1
        else:
            Local = '-1'
            contador = contador + 1

    return Local