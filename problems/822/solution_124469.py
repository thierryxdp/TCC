def repetidos(n):
    i=0
    while i < len(n):
        if len(n[i]) == len(n[i+1]):
            num +=1
        i+=1
    return num