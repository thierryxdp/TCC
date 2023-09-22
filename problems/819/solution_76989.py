def filtraMultiplos(listadenumeros,n):
    """Função que dado uma lista de numeros e um número n retorna outra 
       lista contendo todos os elementos da lista original que forem
       divisíveis por n.
       list,int -> list
       
       Parâmetros:
       listadenumeros: Lista de numeros que será filtrada.
       numero: O número que será usado para filtrar a lista.
       
       returns: Uma outra lista contendo todos os elementos da lista 
                original que forem divisíveis por n.
    """
    listafiltrada = ()
    for numeros in listadenumeros:
        if (numeros%n == 0):
            listafiltrada += numeros
    return listafiltrada