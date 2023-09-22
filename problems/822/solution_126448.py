def repetidos(n):
    for i in range(len(n)-1):
        if n[i] == n[i-1]:
            return sum(len(i))