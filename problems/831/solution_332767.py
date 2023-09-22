def lingua_p (s):
    S = str.lower (s)
    i = 0
    for e in S:
        if e in "aeiouáéíóúâêîôûãõ":
            S = S[0:(i+1)] + "p" + e + S[(i+1):len(S)]
            i = i+3
        else:
            S=S
            i = i+1
    return S