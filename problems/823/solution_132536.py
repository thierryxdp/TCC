def faltante(lista):
    '''descobre qual o numero inteiro do intervalo da lista que está faltando'''
    lista.sort()
    n = len(lista) + 1
    listaCorreta = list(range(1, n + 1))
    i = 1
    while i < len(listaCorreta):
        if(i+1 == len(listaCorreta)):
           	return listaCorreta[i] + 1
        if(listaCorreta[i] not in lista):
            return listaCorreta[i]
        i = i+1