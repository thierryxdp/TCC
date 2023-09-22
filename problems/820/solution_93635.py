def posLetra(string,letra,numero):
    indice=0
    posicao=0
    contagem=0
    if frase.count(letra)>=numero:
        while indice<numero:
            if frase[posicao]==letra:
                contagem+=1
                posicao=str.find(frase[posicao:],letra)+1
                contagem+=posicao
                indice+=1
            return x-1
    else:
        return -1