def insere(lista_numero, n):
    """ define uma função que dada uma lista ordenada crescente de numeros, inclua um numero n na posição correta do jeito que continue ordenada """
    lista_numero1 = lista_numero.append(n)
    return lista_numero1.sort(lista_numero1)