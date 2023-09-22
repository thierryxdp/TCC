def faltante(lista_inteiros):
    lista_inteiros.sort(reverse=True)
    max_int = lista_inteiros[0]
    nao_pertence = []
    for i in range(0,  max_int):
        print(max_int,i)
        if i not in lista_inteiros:
            nao_pertence.append(i)
    if nao_pertence[0]>max_int:
        return nao_pertence[0]+1
    else:
        nao_pertence[0]+1