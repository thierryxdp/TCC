def posLetra(string,letra,n):
    'Recebe uma string, uma letra e um número que indica a ocorrência da letra e retorna em que posição da string aquela ocorrência está;string,string,int->int'''
    i=0
    lista=[]
    while i<len(string):
        resultado=string[i:].find(letra)
        lista.append(resultado+i)
        i+=resultado+2
        corte=lista[0:n-1]
    if len(lista)>n:
        return corte
    elif len(lista)<=n:
        return -1