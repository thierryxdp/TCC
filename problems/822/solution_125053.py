def repetidos(listnum):
    i = 0
    j = 0
    while i+1<len(listnum):
        if listnum[i] == listnum[i+1]:
            j += 1
        if listnum[i] != listnum[i+1]:
            j += 0
        i += 1
    return j