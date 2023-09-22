def posLetra(frase,letra,numero):
    tamanho=len(frase)
    indice=0
    contagem=0
    while indice<tamanho:
        if frase[indice]==letra:
            contagem+=1
        if contagem==numero:
            return indice
        else:
            return -1
    indice+=1