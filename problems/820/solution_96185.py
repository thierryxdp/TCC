def posLetra(Frase,Letra,Numero):
    contador = 1
    while contador <= Numero:
        if Numero <= Frase.count(Letra):
            Troca = str.replace(Frase,Letra,'.',contador)
            Local = str.find(Troca,Letra)
            contador = contador+1
        else:            
            Local = '-1'
            contador = contador + 1
    return Local