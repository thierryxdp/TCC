def posLetra (frase, letra, numero):
    posicao=0
    tamanho=len(frase)
    indice=0
    contagem=0
    while indice<tamanho:
        if frase.count(letra)>=numero:
            contagem = contagem + 1
            posicao=str.find(frase[posicao:],letra)
            contagem = contagem + posicao
            indice = indice +1
            return contagem-1
        indice+=1
    return -1