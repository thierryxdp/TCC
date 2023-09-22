def posLetra(frase,letra,n):
    '''retrona a posicao da ocorrencia n da letra na frase;
    str,str,int->int'''
    lista=list(frase)
    qtd=list.count(frase,letra)
    tam=len(lista)
    if n<=qtd:
        i=0
        while i<tam:
            if lista[i]==letra:
                lista[i]=i
            i=i+1
        return list.index(lista,i)
    else:
        return -1