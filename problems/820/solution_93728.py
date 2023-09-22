def posLetra (frase, letra, numero):
    posiçao=0
    tamanho=len(frase)
    indice=0
    contagem=0
    while indice<tamanho:
        if frase.count(letra)>=numero:
            contagem = contagem + 1
            posiçao=str.find(frase[posiçao:],letra)
            contagem = contagem + posiçao
            indice = indice +1
            return contagem-1
        indice+=1
    return -1