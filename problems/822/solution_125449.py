def repetidos (lista):
    ''' devolve a quantidade de vogais presentes no texto.
    str --> int'''
    qtd_vogais = 0
    i = 0
    while i < len(lista):
        n=lista.count(lista[i])
        return n