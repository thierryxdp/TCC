def faltante(pecas):
    '''Funcao que, dada a lista com as pecas de um quebra-cabeças
    enumeradas, retorna a peca faltante. 
    List -> Int'''
    lista_ordem = list.sort(pecas)
    quantidade_pecas = len(pecas)
    Lista2 = []
    IndiceParte1 = 0
    IndiceParte2 = 0
    proximo = 0

#Parte 1    
#Obter uma lista cujo ultimo elemento seja igual ao valor da
#quantidade de elementos da lista inicial
    while IndiceParte1 < quantidade_pecas:
        Lista2 = Lista2 + [proximo+1,]
        IndiceParte1 = IndiceParte1 + 1
        proximo = proximo + 1

#Parte 2
#Comparar a lista obtida acima com a lista incial. O elemento que 
#nao for igual sera correspondente a peca faltante.
    while pecas[IndiceParte2] == Lista2[IndiceParte2] and IndiceParte2<=len(pecas):
        IndiceParte2 = IndiceParte2 + 1
    return Lista2[IndiceParte2]