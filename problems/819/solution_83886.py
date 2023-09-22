def filtraMultiplos(l,n):
    'filtra uma lista <l> de números multiplos de um numero <n> e retorna uma lista com seus multiplos. Lista -> Lista'
    lista2 = []
    for i in l:
        if i%n == 0:
            lista2.append(i)
    return lista2