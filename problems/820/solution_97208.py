def posLetra(frase,letra,n):
    '''retrona a posicao da ocorrencia n da letra na frase;
    str,str,int->int'''
    lista=list(frase)
    qtd=list.count(lista,letra)
    tam=len(lista)
    i=0
    inds=[]
    if n<=qtd and qtd>0:
        while i<tam:
            if lista[i]==letra:
                list.append(inds,i)
            i=i+1
        return inds[n-1]
    else:
        return -1