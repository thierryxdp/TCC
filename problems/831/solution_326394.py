def lingua_p(palavra):
    n=0
    nova=""
    for i in palavra:
        if palavra[n] in "aeiouAEIOU":
            nova=str.replace(palavra,palavra[n],palavra[n]+"p")
        n=n+1
    return nova