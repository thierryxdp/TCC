def filtraMultiplos(lista,n):
    """Cálculo de função que recebe como entrada uma lista de números e um
    número e retorna uma nova lista contendo todos os números que são multiplos de n.
    
       Parameters:
       lista: uma lista de entrada contendo os valores a serem divididos 
       n: número que será dividido pelos valores da lista.
       
       Returns:
       Retorna uma lista contendo os valores que são divisiveis por n, dado que:
       list, int -> list."""
    multiplos=list()
    numero=0
    while numero < len(lista):
        if (numero % n == 0):
            multiplos.append(numero)
    return list(multiplos)