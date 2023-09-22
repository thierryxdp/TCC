def posLetra(frase,letra, n):
    '''retorna o indice da ocrrencia n da letra na frase'''
    qtd=str.count(frase,letra)
    frasi=list(frase)
    tam=len(frasi)
    inds=[]
    i=0
    if qtd<=tam:
        while frasi[i]==letra:
            list.append(inds,frasi[i])
            str.replace(inds,letra,'tx'*i)
            i=i+1
        ind=list.index(indy,'tx'*n)
        return ind
    else:
        return -1