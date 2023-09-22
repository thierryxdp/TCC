def posLetra(frase,letra,n):
    '''funçao em que dada uma string, uma letra e número que indica a ocorrência desejada da letra,
    e retorna a posição da string, caso exista menos ocorrências da letra do que de a ocorrência pedida,
    a função deve retorna (-1); str,str,int-> list'''
    lista = []
    i = 0
    while i<len(frase):
        if frase[i]==letra:
            lista=lista+[i]
        if (len(lista)+1)<=n:
            v = -1
        if (len(lista)+1)>n:
            v= lista[n-1]
        i=i+1
    return v