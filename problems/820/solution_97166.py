def posLetra(frase,letra,ocorrencia):
    '''retorna a posicao da ocorrencia da letra na frase;
    string,string,int->int'''
    lista=list(frase)
    qtd=list.count(lista,letra)
    if qtd>0 and ocorrencia<=qtd:
        frase.replace(letra, 'XXX', ocorrencia).find(letra)
    else:
        return -1