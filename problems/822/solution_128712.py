def repetidos(lista):
    """recebe uma lista e retorna o número de vezes que um número inteiro x se repete dentro dela.
    list->int"""
    b=0
    L=lista[1:]
    i=list(range(len(L)))
    t=int
    for x in lista:
        for t in i:
            if L[t]==lista[t]:
                b=b+1


        return b