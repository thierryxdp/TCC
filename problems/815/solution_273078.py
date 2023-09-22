def insere (lista_numero: list, n: int)->list:
    "Dada uma lista ordenada, inclui n de forma contínua"
    lista_numero.append(n)
    list.sort(lista_numero)
    return lista_numero