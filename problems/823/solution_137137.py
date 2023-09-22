def faltante(lista_inteiros):
    lista_inteiros.sort(reverse=True)
    max_int = lista_inteiros[0]
    nao_pertence = []
    for i in range(1,  max_int):
        if i not in lista_inteiros:
            nao_pertence.append(i)
    return nao_pertence[0]


print(faltante([3,1]))
print(faltante([1,2,3,5]))
print(faltante([2,4,3]))