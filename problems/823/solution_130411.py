def faltante(lista):
    """esta função recebe uma lista de números e retorna os números faltantes desta lista
    list-> int"""
    indice=0
    lista1=list(range(1,len(lista)+1))
    if lista[0]!=1:
        A=1
    elif lista==lista1:
        A=len(lista)+1
    else:
        while lista[indice]==indice+1:
            indice+=1
            A=índice+1
    return A