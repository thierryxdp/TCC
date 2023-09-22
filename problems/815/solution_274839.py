def insere(lista_numero,n):
    "inclue um numero <n> na lista<lista_numero> e a mantem ordenada após inserção. list ->list"
    lista_numero.append(n)
    y = lista_numero.sort()
    return y