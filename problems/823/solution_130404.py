def faltante(lista):
    """esta função recebe uma lista de números e retorna os números faltantes desta lista
    list-> int"""
    lista.sort()
    indice=0
    lista1=range(1,len(lista)+1)
    if lista[0]!=1:
        a=1
    if lista==lista1:
        a=len(lista)+1
    else:
        b=lista[indice]
        while b+1==indice+2:
            a=indice+2
                      indice+=1
        return a