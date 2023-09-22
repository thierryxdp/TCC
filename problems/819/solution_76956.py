def filtraMultiplos(lista,n):
    """Cálculo de função que recebe como entrada uma lista de números e um
    número e retorna uma nova lista contendo todos os números que são multiplos de n.
    
       Parameters:
       lista: uma lista de entrada contendo os valores a serem divididos 
       n: número que será dividido pelos valores da lista.
       
       Returns:
       Retorna uma lista contendo os valores que são divisiveis por n, dado que:
       list, int -> list."""
    indice=0
    multiplos=list()
    while indice < len(lista):
        if (indice % n == 0):
            list.append(multiplos,indice)
        indice=indice+1
    return list(multiplos)