def faltante(lista):
    """esta função recebe uma lista de números e retorna os números faltantes desta lista
    list-> int"""
    lista.sort()
    indice=0
    lista1=list(range(1,len(lista)+1))
    if lista[0]!=1:
        return 1
    elif lista==lista1:
        return len(lista)+1
    else:
        while lista[indice]==indice+1 and indice+1!=len(lista):
            indice+=1
    return indice+1