faltante(pecas):
    '''Funcao que, dada a lista com as pecas de um quebra-cabeças
    enumeradas, retorna a peca faltante. 
    List -> Int'''
    lista_ordem = list.sort(lista)
    quantidade = len(lista)
    ListaCopia = []
    IndiceParte1 = 0
    IndiceParte2 = 0
    while IndiceParte1 < quantidade:
        ListaCopia = ListaCopia + [lista[IndiceParte1],]
        IndiceParte1 = IndiceParte1 + 1

    while lista[IndiceParte2] == ListaCopia[IndiceParte2]:
        IndiceParte2 = IndiceParte2 + 1
    return ListaCopia[IndiceParte2]