def posLetra(string,letra,n):
    'Recebe uma string, uma letra e um número que indica a ocorrência da letra e retorna em que posição da string aquela ocorrência está;string,string,int->int'''
    i=0
    lista=[]
    resultado=string[i:].find(letra)
    while i<len(string):
        lista.append(resultado+i)
        i+=resultado+2
    if len(lista)>=n:
        return lista[n-1]
    elif len(lista)<n:
        return -1