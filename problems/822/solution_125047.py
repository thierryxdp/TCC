def repetidos(listnum):
    i = 0
    j = 0
    while i<len(listnum):
        if listnum[i] == listnum[i+1]:
            j += 1
    return j