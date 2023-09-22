def filtraMultiplos(listadenumeros,n):
    """Função que dado uma lista de numeros e um número n retorna uma 
       outra lista filtrada contendo todos os elementos da lista original
       divisíveis por n.
       list,int->list
       
       Parâmetros:
       listadenumeros: Lista de números que será filtrada.
       n: Número que irá filtrar todos os elementos da lista.
       
       Returns: Uma outra lista contendo todos os elementos da lista 
                original divisíveis por n.
    """
    contador = 0
    listafiltrada = []
    while contador < len(listadenumeros):
        if listadenumeros[contador]%n == 0:
            listafiltrada.append(listadenumeros[contador])
        contador = contador+1                          
    return listadenumeros