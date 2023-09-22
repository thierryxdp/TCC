def repetidos(lst):
    vezes = 0
    for x in lst:
        if lst(x)==lst(x-1):
            vezes += 1
    return vezes