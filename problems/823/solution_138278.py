def faltante(lista):
    """
    Dada uma sequencia em uma lista,nessa ordem ira estar faltando um termo
    o qual a função 'faltante' ira retornar.
    list->float
    """
    if lista[-1] == (lista[-2] - 1):
        return (lista[-1]) + 1
    soma = (lista[-1] *(lista[0]+lista[-1]))/2
    
    soma_parcial = 0
    contador = 0
    while contador <= len(lista) - 1:
        soma_parcial = soma_parcial + lista[contador]
        contador = contador + 1
    return soma - soma_parcial