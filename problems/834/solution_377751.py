def media_matriz(A):
    '''REtorna a média de todos os números de uma matriz de números inteiros, não vazia. list(list)->float.'''
    lista=[]
    soma=[]
    for elem in range(len(A)):
        numero_termos=len(A[elem])
        S=sum(A[elem])
        list.append(lista,numero_termos)
        list.append(soma,S)
    soma_total=(sum(soma))
    numero_total_termos=(sum(lista))
    media=(soma_total/numero_total_termos)
    return(round(media,2))