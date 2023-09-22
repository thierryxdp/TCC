def filtra_pares(numeros):
    """Função que recebe um conjunto de elementos inteiros e retorna
outro conjunto contendo apenas os elementos pares."""
    
	numeros = (n1,n2,n3,n4) 
    a1 = n1 % 2
    a2 = n2 % 2
    a3 = n3 % 2
    a4 = n4 % 2
 
    if a1 == 0 and a2 == 0 and a3 == 0 and a4 == 0:
        return (n1,n2,n3,n4)
    elif a1 == 0 and a3 == 0 and a4 == 0:
        return (n1,n3,n4)
    elif a1 == 0 and a2 == 0 and a4 == 0:
        return (n1,n2,n4)
    elif a1 == 0 and a2 == 0 and a3 == 0:
        return (n1,n2,n3)
    elif a2 == 0 and a3 == 0 and a4 == 0:
        return (n2,n3,n4)
    elif a1 == 0 and a2 == 0:
        return (n1,n2)
    elif a2 == 0 and a3 == 0:
        return (n2,n3)
    elif a3 == 0 and a4 == 0:
        return (n3,n4)
    elif a1 == 0 and a4 == 0:
        return (n1,n4)
    elif a2 == 0 and a4 == 0:
        return (n2,n4)
    elif a1 == 0 and a3 == 0:
        return (n1,n3)
    elif a1 == 0:
        return (n1)
    elif a2 == 0:
        return (n2)
    elif a3 == 0:
        return (n3)
    elif a4 == 0:
        return (n4)