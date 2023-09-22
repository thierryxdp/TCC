def faltante(lista):
    '''função que retorna o valor faltante 
    numa lista:
    valor de entrada: list
    valor de saída: int'''
	if lista[-1]<0 and len(lista)==1:
        return lista[-1]-1
    if lista[-1] < len(lista) + 1:
        return len(lista) + 1
    i = 0
    falta = 0
    while i < len(lista) - 1:
        if lista[i + 1] - lista[i] > 1:
            falta = falta + lista[i] + 1
        i = i + 1
    return falta