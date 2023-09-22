def lingua_p(palavra):
    n=0
    nova=""
    for i in palavra:
        if palavra[n] in "aeiouAEIOU":
            nova=palavra[n]+"p"+palavra[n:]
        n=n+1
    return nova