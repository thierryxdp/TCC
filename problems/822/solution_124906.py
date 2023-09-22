def repetidos(lista_de_numeros):
    lista_em_ordem=list.sort(lista_de_numeros)
    repeticoes=0
    i=0
    while i<lien(lista_de_numeros):
        if lista_em_ordem[i]==lista_em_ordem[i+1]:
            repeticoes=repeticoes+1
            i=i+1
        else:
            i=i+1
    return repeticoes