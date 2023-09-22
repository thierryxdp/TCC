def posLetra(frase,letra,ocorrencia):
    '''retorna a posicao da ocorrencia da letra na frase;
    string,string,int->int'''
    lista=list(frase)
    listaletra=list(letra)
    if listaletra in lista:
        ind=list.index(lista,listaletra,ocorrencia)
        return ind+1
    else:
        return -1