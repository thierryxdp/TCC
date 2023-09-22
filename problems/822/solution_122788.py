def repetidos(lista):

    counter = 0
    seen = set()
    for elm in seq:
        if elm in seen:
            counter += 1
        else:
            seen.add(elm)
    return counter

res = repetidos([''])
print(res)