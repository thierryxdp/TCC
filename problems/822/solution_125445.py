def repetidos (lista):
    ''' devolve a quantidade de vogais presentes no texto.
    str --> int'''
    qtd_vogais = 0
    i = 0
    while i < len(lista):
        n=lista.count(lista[i])>1
        qtd_vogais = qtd_vogais + 1
        i = i + 1
    return n