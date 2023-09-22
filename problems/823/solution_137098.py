def faltante(lista):
    "Identifica qual o numero da peça do quebra-cabeça está"
    "faltando"
    "list -> int"
    list.sort(lista)
    i=0
    d=1
    while i<len(lista):
        if lista[0] == 2:
            a = 1
        elif lista[i]%d != 0:
            a = (lista[i] - 1)
        else:
            a = (len(lista) + 1)
        i += 1
        d += 1
    return a