def divisiveis_por_n(n,lista):
    '''Dados um número n e uma lista de números, retorna
os numeros divisiveis por n que estejam na lista.
int, list -> list'''
    resultado=[]
    i=0
    while i<len(lista):
        elemento = lista[i]
        if n%elemento ==0:
            resultado.append(elemento)
        i=i+1
    return resultado