def faltante(lista):
    """Função que dados uma lista retorne o número faltante.
    list-> int"""
    ct = 0
    lista1 = range(1, len(lista)+1)

    while ct < len(lista):
       
        if lista[ct] == lista1[ct] and ct == len(lista)-1:
            return lista[ct] + 1

        if lista[ct] != lista1[ct]:
            return lista1[ct]
        ct = ct + 1