def insere(lista_numero,n):
    'dada uma lista em ordem rescente, adiciona n de forma a manter a ordem, lista, int -> lista'
    return sorted(lista_numero + [n])