def faltante(lista):
    ''' dada uma lista que tem n-1 pecas, ira informar a peca n que falta no quebra-cabecas,
list->int '''
    lista_corrigida = lista.sort()
    auxiliar= []
    i = 1
    while i<=len(lista)+1:
        auxiliar = auxiliar +[i]
        i = i + 1
        faltante = sum(auxiliar)-sum(lista)
    return faltante