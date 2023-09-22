def acima_da_media(lista):
    '''função que, dada uma lista com as notas dos alunos, retorne as notas
    acima da média.
    list -> list'''
    soma_notas = sum(lista)
    quantos_alunos = len(lista)
    media = soma_notas/quantos_alunos
    
    lista_com_n = lista.insert([0],media)
    lista_ordenada = lista.sort()
    i = lista.index(media)
    acimadamedia = del lista_ordenada[i:]
    return acimadamedia