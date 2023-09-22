def faltante(listaPecas):
    '''dada uma list litaPecas com N-1 termos numeradas de
    1 a N, retorna qual numero inteiro esta faltando
    list->int'''
    list.sort(listaPecas)
    if listaPecas[0]!=1:
        return 1
    elif listaPecas[len(listaPecas)-1]!=len(listaPecas)-1:
        return len(listaPecas)
    else:
        contador = 0
        contador2 = 2
        while listaPecas[contador]==listaPecas[contador+1]-1:
            contador = contador + 1
            contador2 = contador2 + 1
        return contador2