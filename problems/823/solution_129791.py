def faltante(lista):
    """funcao que retorna o numero que falta em um intervalo numero de uma lista;
    list -> int"""

    lista.sort()
    f = sum(lista)//2
    i = 0
    n = []


    while i<len(lista):

        if f not in list(range(1,lista[len(lista)-1]+1)):

             n.append(f)    
            

        i = i+1

    return f