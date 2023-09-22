def  faltante(lista):
    ''' Função recebe lista e retorna elemento q falta list -->int'''
    list.sort(lista)
    lista_ordenada = list(range(1, len(lista)+2))
    i = 0 
    while len(lista_ordenada) > i + 1:
        if lista[i] != lista_ordenasa[i]:
            return lista_ordenada[i]
        i += 1
    return lista_ordenada[-1]