def lingua_p(palavra):
    for i in range(len(palavra)-1,-1,-1):
        if palavra[i] in "aeiouAEIOU":
            palavra=palavra[:i+1]+'p'+palavra[i]+palavra[i+1:]
            i-=1
        else:
            i-=1
    return palavra