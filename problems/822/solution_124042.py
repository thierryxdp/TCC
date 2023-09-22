def repetidos(n: list) -> int:
    i = 0
    total = []
    list.sort(n)
    
    while i < len(repetidos):
        if repetidos[i] == repetidos[i-1]:
            total = total + [1,]
            list.remove(n, repetidos[i])
        i = i + 1
    return len(total)