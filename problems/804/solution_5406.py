def filtra_pares(*tupla):
    #Retorna os valores pares da tupla fornecida.
    #tuple->tuple
    print(tupla)
    comprimento = len(tupla)
    n = 1
    lista_de_numeros = []
    for n in tupla:
        if n % 2 == 0:
            lista_de_numeros.append(n)
        n += 1
    tupla_par = tuple(lista_de_numeros)
    return tupla_par