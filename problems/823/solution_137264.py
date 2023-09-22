def faltante(lista):
    '''
       Função que recebe uma lista e retorna
       o numero inteiro que está faltando
       list -> int
    '''
    L = 0 
    L_Ni = list(range(1,len(lista) + 2))

    while len(L_Ni) > L+1:
        if lista[L] != L_Ni[L]:
            return L_Ni[L]

        L = L + 1

    return L_Ni[-1]