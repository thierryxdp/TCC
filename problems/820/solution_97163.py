def posLetra(frase,letra,ocorrencia):
    '''retorna a posicao da ocorrencia da letra na frase;
    string,string,int->int'''
    lista=list(frase)
    qtd=list.count(lista,letra)
    if qtd>0 or ocorrencia<qtd:
        ind=list.index(lista,letra)
        return ind
    else:
        return -1