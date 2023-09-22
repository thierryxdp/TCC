def intercala(lista1,lista2):
    ''' funcao recebe duas lista de tres elementos e intercala geral uma outra lista com os elementos intercalados
    da lista1 e lista 2. lista,lista-->lista'''
    return lista1[0:1]+lista2[0:1]+lista1[1:2]+lista2[1:2]+lista1[2:]+lista2[2:]