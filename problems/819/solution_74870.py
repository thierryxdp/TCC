def filtraMultiplos(lista,n):
    """Filtra e Retorna os números da lista dada que são multiplos de n;
       list,int->list
       Parâmetros:
       lista: lista qualquer
       n: um número inteiro
    """
    i=0
    multiplos=[]
    while i<=len(lista):
        if lista[i]%n==0:
            multiplos.append(lista[i])
        i=i+1
    return multiplos