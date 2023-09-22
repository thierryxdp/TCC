def posLetra(frase,letra,n):
    ''' Função que retorna a posição da n-ésima ocorrencia da letra na string dada como entrada; str,str,int->int''' 
    l1=[]
    c=0
    while c<len(frase):
        if frase[c]==letra:
            list.append(l1,c)
        c=c+1
    return l1[posicao-1]