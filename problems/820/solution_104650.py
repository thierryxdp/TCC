def posLetra(frase,letra, p):
    '''retorna em que posição da string aquela ocorrência da letra está,
    caso exista menls ocorrência da letra do que a pedida, a função deve retornar -1
    str, str, int-> int'''
    i=0
    lista=[]
    while i<len(frase):
        if letra == frase[i]:
            lista = lista+[i,]
        i = i+1
    if p< len(lista):
        return -1
    else:
        return lista[p-1]