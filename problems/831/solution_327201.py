def lingua_p(palavra):
    for i in range(len(x)-1,-1,-1):
        if palavra[i] in "abcdeABCDE":
            palavra=palavra[:i+1]+'p'+palavra[i]+palavra[i+1:]
            i-=1
        else:
            i-=1
    return palavra