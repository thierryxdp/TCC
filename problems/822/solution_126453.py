def repetidos(n):
    for i in range(len(n)-1):
        while n[i] == n[i-1]:
            return n[i-1]