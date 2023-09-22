def posLetra(frase,letra,n):

    lst=[]
    i=0
    vazio=''
    if n <= frase.count(letra):
        while i<len(frase):
            if frase[i] in letra:
                vazio=frase[i]           
                list.append(lst,i)
            i=i+1
        return lst[n-1]
    else:
        return -1