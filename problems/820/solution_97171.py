def posLetra(frase,letra,ocorrencia):
    '''retorna a posicao da ocorrencia da letra na frase;
    string,string,int->int'''
    lista=list(frase)
    qtd=list.count(lista,letra)
    if qtd>0 and ocorrencia<=qtd:
        nova=str.split(frase,letra)
        novanova=nova[ocorrencia-1]
        novanova[0]='IGOR'
        listapp=list.frase
        ind=list.index(listapp,'IGOR')
        return ind
    else:
        return -1