def maiores(lista_numeros, n): 
    """funcao que dada uma lista de numeros e um numero inteiro retorna outra lista com todos os numeros da lista original maiores que n;
       list, int->list"""
    if n in lista_numeros:
        lista_numeros.sort()
        lista_numeros.index(n)
        return lista_numeros[lista_numeros.index(n):]
    elif n not in lista_numeros:
        lista_numeros.append(n)
        lista_numero.sort()
        lista_numeros.index(n)
        return lista_numeros[lista_numeros.index(n):]