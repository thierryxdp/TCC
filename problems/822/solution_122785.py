def repetidos(lista):
    return len(lista) - len(set(lista))

res = repetidos(["1,4,3,3,2,3,3,3,3,5,4,6,6,7,6,8,8,7"])
print(res)