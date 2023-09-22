def posLetra(string,letra,n):
    '''Dada uma string, indique a ocorrência da letra na posição n; str,str,int -> int'''
    i=0
    string=list(string)
    lista=[]
    while i<len(string):
        if letra in string:
            index=list.index(string,letra)
        i=i+1
        return index
    else:
        return -1