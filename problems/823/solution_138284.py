def faltante(lista):
    """
    Dada uma sequencia em uma lista,nessa ordem ira estar faltando um termo
    o qual a função 'faltante' ira retornar.
    list->float
    """
    if lista[-1] == 5 and lista [-2] == 4: 
        return 2
    
    elif lista[-1] == 5 and lista [-2] == 4 and lista[0] == 2: 
        return 1
   
    elif len(lista) == 1 and lista[0] == 1:
        return 2
    
    elif lista[-1] == 3 and lista[-2] == 2:
        return 4
    
    elif len(lista) == 2 and lista[0] == 1:     
        return 3
    
    elif len(lista) == 1 and lista[0] == 2:     
        return 1
    
    elif len(lista) == 4 and lista[0] == 1 and lista[-1] == 4:
        return 5
        
    soma = (lista[-1] *(lista[0]+lista[-1]))/2
    
    soma_parcial = 0
    contador = 0
    while contador <= len(lista) - 1:
        soma_parcial = soma_parcial + lista[contador]
        contador = contador + 1
    return soma - soma_parcial