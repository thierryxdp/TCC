def posLetra(frase,letra,n):
    '''str,str,int->'''
    posicao=str()
    lista=[]
    i=0
    while i<len(frase):
        if letra == frase[i]:
            list.append(lista,str.find(frase,letra,n))
        i=i+1
    return lista[len(lista)-1]