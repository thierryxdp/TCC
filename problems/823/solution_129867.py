def faltante(lista):
    quantidade = len(lista)
    lista_completa = list(range(0,quantidade+2))
    return sum(lista_completa) - sum(quantidade)