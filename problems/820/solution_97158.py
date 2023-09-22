def posLetra(frase,letra,ocorrencia):
    '''retorna a posicao da ocorrencia da letra na frase;
    string,string,int->int'''
    lista=list(frase)
    if letra in lista:
        ind=list.index(lista,letra)
        return ind+1
    else:
        return -1