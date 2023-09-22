def posLetra(frase,letra,numero):
    indice=0
    posicao=0
    contagem=0
    while indice<numero:
        if frase.count(letra)>=numero:
            contagem+=1
            posicao=str.find(frase[posicao:],letra)
            contagem+=posicao
            indice+=1
            return contagem=contagem-1
        else:
            return -1