def insere (lista_numero: list, n: int)-> list:
    '''Dada uma lista de números inteiros crescentes e um número
    inteiro n, retorna uma lista com n incluido na posição correta'''
    novalista= lista_numero.append(n)
    novalista= list.sort(novalista)
    return novalista