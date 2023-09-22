def posLetra(Frase,Letra,Numero):
    contador = 0
    while contador < Numero:
        if Frase.count(Letra)<=Numero:
        	str.replace(Frase,'.',Letra)
        	Local = str.find(Frase, Letra)
        	contador = contador + 1
        else:
            Local = '-1'

    return