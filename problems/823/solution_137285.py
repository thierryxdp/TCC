def faltante(listaPecas):
    '''dada uma list litaPecas com N-1 termos numeradas de
    1 a N, retorna qual numero inteiro esta faltando
    list->int'''
    list.sort(listaPecas)
    contador = 0
    while listaPecas[0]==listaPecas[1]-1:
        contador = contador + 1
    return contador + 1