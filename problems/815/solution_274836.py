insere(lista_numero,n):
    "inclue um numero <n> na lista<lista_numero> e a mantem ordenada após inserção. list ->list"
    x = lista_numero.append(n)
    y = list.sort(x)
    return y