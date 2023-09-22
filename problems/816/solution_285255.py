def maiores(lista_numero,n):
    '''
    nese problema foi adicionado o numero na lista_numero e coloco todos os numeros em ordem.
    depois verificamos em qual possição o numero se encontra, e colocamos todos os outros numero no return.

    '''
    
    list.append(lista_numero, n)
    
    list.sort(lista_numero)
    
    A = list.index(lista_numero,n)
    
    return lista_numero[A+1:]