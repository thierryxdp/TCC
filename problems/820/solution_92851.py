def posLetra(string,letra,n):
    'Recebe uma string, uma letra e um número que indica a ocorrência da letra e retorna em que posição da string aquela ocorrência está;string,string,int->int'''
    i=
    lista=[]
    while i<len(string):
        resultado=string[i:].find(letra)
        lista.append(resultado+i)
        i+=resultado+2
        corte=lista[0:n]
    if len(lista)>n:
        return corte[-1]
    elif len(lista)<=n:
        return -1