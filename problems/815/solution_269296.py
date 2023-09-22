def insere(lista_numero, n):
    if n in lista_numero:
        lista_numero.append(n)
        lista_numero.sort()
    elif n not in lista_numero:
        if n > 0:
            for i in range(n+1):
                if i not in lista_numero:
                    lista_numero.append(i)
                    lista_numero.sort()
        elif n < 0:
            for i in range(n, 1):
                if i not in lista_numero:
                    lista_numero.append(i)
                    lista_numero.sort()
    return lista_numero