def maiores(lista_numeros, n):
    """ Funcao que recebe uma lista de inteiros e um numero inteiro n.
    	Retorna uma nova lista com todos os numeros inteiros maiores que n;
        list, int -> list
    """
    nova_lista = []
    for numero in lista_numeros:
        if numero > n:
            nova_lista.append(numero)
            
    nova_lista.sort()   
    
    return nova_lista