def repetidos (lista):
    ''' devolve a quantidade de vogais presentes no texto.
    str --> int'''
    qtd_vogais = 0
    i = 0
    while i < len(lista):
        if lista.count(lista[i])>2: 
            qtd_vogais = qtd_vogais + 1
        i = i + 1
    return qtd_vogais