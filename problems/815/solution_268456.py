def insere(lista_numero, n):
    """Função que irá receber uma lista ordenada de números inteiros e um número
		inteiro 'n'. Ela irá incluir o número na lista na posição correta,
		de forma que a lista continue ordenada.
        list, int -> list
   		
        Parameters:
        lista_numero: lista com os números inteiros ordenados
        n: número que irá ser inserido na lista já existente
        
        Returns:
        lista ordenada com os números originais e com o novo número
    """

    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero