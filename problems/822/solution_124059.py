def repetidos(n: list) -> int:
    i = 0
    total = []
    list.sort(n)
    
    while i < len(n):
        if n[i-1] == n[1]:
            total = total + [1,]
            list.remove(n, n[i])
        i = i + 1
    return len(total)