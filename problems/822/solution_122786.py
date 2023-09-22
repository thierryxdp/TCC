def repetidos(lista):
    return len(lista) - len(set(lista))

res = repetidos([])
print(res)