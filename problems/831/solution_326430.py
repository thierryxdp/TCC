def lingua_p(palavra):
    for i in range(len(palavra)):
        if palavra[i] in "AEIOUaeiou":
            palavra=palavra[:i+1]+"p"+palavra[i]+palavra[i+1:]
    return palavra