# Dadas duas listas, L1 e L2, de 3 elementos cada, queremos
# uma lista L3 com os elementos de ambas intercalados.
# Resolução:
# 1. Concatenar o intervalo correspondente ao primeiro elemento
#    da lista1 ao primeiro da lista2;
# 2. Repetir o processo concatenando os intervalos das listas 1
#    e 2 alternada e ordenadamente;
# 3. Devolver.

# list, list -> list

def intercala(lista1, lista2):
    """Dadas lista1 e lista2, respectivamente, com 3 elementos
    devolve lista3 composta dos elementos de ambas intercalados
    list, list -> list"""
    lista3 = lista1[0:1] + lista2[0:1] + lista1[1:2] + lista2[1:2] + lista1[2:3] + lista2[2:3]
    return lista3