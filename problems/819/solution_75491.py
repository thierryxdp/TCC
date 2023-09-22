def filtraMultiplos(numeros,n):
    """Retorna uma lista com os números dentro da lista numeros que são divisíveis por n; list, float -> list """
    multiplos=[];
    prox=0;
    while prox<len(numeros):
        if numeros[prox]%n==0:
            list.append(multiplos,numeros[prox]);
        prox+=1
    return multiplos;