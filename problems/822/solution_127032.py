def repetidos(lista):
    """Recebe uma função com numeros e retorna quantas vezes há prepetições nele, ou seja, se o número anterior é igual ao número antes dele;
    	list -> int"""
    indice=1
    parador=len(lista)-1
    numeroderepeticoes=0
    while indice<=parador:
        if lista[indice-1]==lista[indice]:
            numeroderepeticoes=numeroderepeticoes+1
        indice=indice+1
    return numeroderepeticoes