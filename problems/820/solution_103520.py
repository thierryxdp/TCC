def posLetra(string,letra,n):
    '''funcao que retorna em qual posicao da frase a letra se repete em relacao ao numero dado
    str,str,int->int'''
    i=0
    acumulador=0
    while i<len(string) and acumulador<n:
        if string[i] == letra:
            acumulador=acumulador+1
        i=i+1
        return str(string)+str(acumulador)
    if acumulador<n:
        return -1