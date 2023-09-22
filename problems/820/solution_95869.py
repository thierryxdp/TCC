def posLetra(frase,letra,n):
    '''Função que recebe como entrada uma string, uma letra e um número que indica a ocorrência desejda da letra, e retorna em que posição da string aquela ocorrência da letra está; str,str,int->int''' 
    l1=[]
    c=0
    if str.count(frase,letra)<n:
        return -1
    while c<len(frase):
        if frase[c]==letra:
            list.append(l1,c)
        c=c+1
    return l1[n-1]