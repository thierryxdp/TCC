def uppCons(frase):
    '''retorna a frase com todas as consoantes maiúsculas, str->str''''
    frase1=list(frase)
    lista=[]
    i=0
    while len(frase1)>i:
        if frase1[i] in 'bcdfghjklmnpqrstvwxyzç':
            frase2=str.upper(frase1[i])
            frase1[i]=frase2
            list.insert(lista,i,frase1[i])
            i=i+1
        else:
            list.insert(lista,i,frase[i])
            i=i+1
        frase3=str.join('',frase1)

    return frase3