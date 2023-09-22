def posLetra(string,letra,numero):
    indice=0
    posicao=0
    contagem=0
    while indice<numero:
        if list.count(lista,letra)>=numero:
            contagem+=1
            posicao=str.find(frase[posicao:],letra)+1
            contagem+=posicao
            indice+=1
    return -1