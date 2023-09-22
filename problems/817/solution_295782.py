def maiores(lista_numeros, n): 
    """funcao que dada uma lista de numeros e um numero inteiro retorna outra lista com todos os numeros da lista original maiores que n;
       list, int->list"""
    if n in lista_numeros:
        lista_numeros.sort()
        lista_numeros.index(n)
        return lista_numeros[lista_numeros.index(n)+1:]
    
    elif n not in lista_numeros:
        lista_numeros.append(n)
        lista_numeros.sort()
        lista_numeros.index(n)
        return lista_numeros[lista_numeros.index(n)+1:]
    
def acima_da_media(lista_notas): 
    media= (sum(lista_notas))/(len(lista_notas))
    return maiores(lista_notas, media)