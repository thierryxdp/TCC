def posLetra(Frase,Letra,Numero):
    contador = 0
    aparicao = 1
    while contador <= Numero:
        if Numero < Frase.count(Letra):
            Troca = str.replace(Frase,Letra,'.',aparicao)
            Local = str.find(Troca,Letra)
            contador = contador+1
            aparicao = aparicao+1
        elif Numero == Frase.count(Letra):
            Troca = str.replace(Frase,Letra,'.',aparicao-1)
            Local = str.find(Troca,Letra)
            contador = contador+1
            aparicao = aparicao+1
            
        else:            
            Local = '-1'
            contador = contador + 1
            aparicao = aparicao + 1
    return Local