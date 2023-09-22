def posLetra(string,letra,numero):
    contagem=0
    posicao=0
    if frase.count(lista,letra)>=numero:
        while contagem<numero:
            if frase[posicao]==letra:
                x+=1
                posicao=str.find(frase[posicao:],letra)+1
                x+=posicao
                contagem+=1
            return x-1
    else:
        return -1