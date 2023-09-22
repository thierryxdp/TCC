def repetidos(listanum):
    i=1
    igual=0
    while i<len(listanum):
        if listanum[i]==listanum[(i-1)]:
            igual=igual+1
        i=i+1
    return igual