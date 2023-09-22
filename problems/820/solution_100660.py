def posLetra(frase,letra,ocorrencia):
    '''Dado uma frase,uma letre e um número inteiro que indicando sua ocorrência.
Retorna a posição da frase em que aquela ocorrência de letra se encontra
str,str,int-->int'''
    if frase.count(letra) < ocorrencia:
        return -1
    i=0
    letras=[]
    lista= list(frase)
    while i < len(lista) and len(letras) < ocorrencia:
        if letra==lista[i]:
            list.append(letras, lista[i],)
        i= i+1
    return i-1